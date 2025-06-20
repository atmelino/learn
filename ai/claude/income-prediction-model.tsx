import React, { useState, useEffect } from 'react';
import { Play, Download, BarChart3, Settings, Brain } from 'lucide-react';
import * as tf from 'tensorflow';

const IncomePredictionModel = () => {
  const [csvData, setCsvData] = useState(null);
  const [model, setModel] = useState(null);
  const [isTraining, setIsTraining] = useState(false);
  const [trainingHistory, setTrainingHistory] = useState([]);
  const [modelMetrics, setModelMetrics] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [predictionInputs, setPredictionInputs] = useState({
    age: 45,
    aspect: 25,
    subscriptions: 2,
    save_rate: 30,
    dist_healthy: 10,
    dist_unhealthy: 5,
    pop_dense: 0.8,
    retail_dense: 0.6,
    crime: 0.3
  });

  // Load and process CSV data
  useEffect(() => {
    loadCsvData();
  }, []);

  const loadCsvData = async () => {
    try {
      const response = await window.fs.readFile('jh-simple-dataset.csv', { encoding: 'utf8' });
      const lines = response.trim().split('\n');
      const headers = lines[0].split(',');
      const data = lines.slice(1).map(line => {
        const values = line.split(',');
        const row = {};
        headers.forEach((header, index) => {
          row[header.trim()] = values[index];
        });
        return row;
      });
      
      // Filter out rows with missing income data
      const cleanData = data.filter(row => row.income && row.income !== '' && !isNaN(parseFloat(row.income)));
      setCsvData(cleanData);
    } catch (error) {
      console.error('Error loading CSV:', error);
    }
  };

  const preprocessData = (data) => {
    // Select numerical features for prediction
    const features = ['age', 'aspect', 'subscriptions', 'save_rate', 'dist_healthy', 'dist_unhealthy', 'pop_dense', 'retail_dense', 'crime'];
    
    const X = [];
    const y = [];
    
    data.forEach(row => {
      const featureRow = features.map(feature => {
        const value = parseFloat(row[feature]);
        return isNaN(value) ? 0 : value;
      });
      const income = parseFloat(row.income);
      
      if (!isNaN(income)) {
        X.push(featureRow);
        y.push(income);
      }
    });
    
    return { X, y, features };
  };

  const normalizeData = (data) => {
    const tensor = tf.tensor2d(data);
    const { mean, variance } = tf.moments(tensor, 0);
    const normalized = tensor.sub(mean).div(variance.sqrt());
    return { normalized, mean, variance };
  };

  const createModel = (inputShape) => {
    const model = tf.sequential({
      layers: [
        tf.layers.dense({
          inputShape: [inputShape],
          units: 64,
          activation: 'relu',
          kernelRegularizer: tf.regularizers.l2({ l2: 0.001 })
        }),
        tf.layers.dropout({ rate: 0.3 }),
        tf.layers.dense({
          units: 32,
          activation: 'relu',
          kernelRegularizer: tf.regularizers.l2({ l2: 0.001 })
        }),
        tf.layers.dropout({ rate: 0.2 }),
        tf.layers.dense({
          units: 16,
          activation: 'relu'
        }),
        tf.layers.dense({
          units: 1,
          activation: 'linear'
        })
      ]
    });

    model.compile({
      optimizer: tf.train.adam(0.001),
      loss: 'meanSquaredError',
      metrics: ['mae']
    });

    return model;
  };

  const trainModel = async () => {
    if (!csvData) return;
    
    setIsTraining(true);
    setTrainingHistory([]);
    
    try {
      const { X, y, features } = preprocessData(csvData);
      
      // Normalize features
      const { normalized: XNorm, mean: XMean, variance: XVar } = normalizeData(X);
      const yTensor = tf.tensor1d(y);
      
      // Split data (80% train, 20% test)
      const totalSamples = X.length;
      const trainSize = Math.floor(totalSamples * 0.8);
      
      const XTrain = XNorm.slice([0, 0], [trainSize, -1]);
      const yTrain = yTensor.slice([0], [trainSize]);
      const XTest = XNorm.slice([trainSize, 0], [-1, -1]);
      const yTest = yTensor.slice([trainSize], [-1]);
      
      // Create and train model
      const newModel = createModel(features.length);
      
      const history = await newModel.fit(XTrain, yTrain, {
        epochs: 100,
        batchSize: 16,
        validationData: [XTest, yTest],
        callbacks: {
          onEpochEnd: (epoch, logs) => {
            setTrainingHistory(prev => [...prev, {
              epoch: epoch + 1,
              loss: logs.loss,
              val_loss: logs.val_loss,
              mae: logs.mae,
              val_mae: logs.val_mae
            }]);
          }
        }
      });
      
      // Calculate final metrics
      const predictions = newModel.predict(XTest);
      const mse = tf.losses.meanSquaredError(yTest, predictions);
      const mae = tf.losses.absoluteDifference(yTest, predictions).mean();
      
      const mseValue = await mse.data();
      const maeValue = await mae.data();
      
      setModelMetrics({
        mse: mseValue[0],
        mae: maeValue[0],
        rmse: Math.sqrt(mseValue[0])
      });
      
      // Store normalization parameters with model
      newModel.normalizationParams = { XMean, XVar };
      setModel(newModel);
      
      // Clean up tensors
      XNorm.dispose();
      yTensor.dispose();
      XTrain.dispose();
      yTrain.dispose();
      XTest.dispose();
      yTest.dispose();
      predictions.dispose();
      mse.dispose();
      mae.dispose();
      
    } catch (error) {
      console.error('Training error:', error);
    } finally {
      setIsTraining(false);
    }
  };

  const makePrediction = () => {
    if (!model) return;
    
    const inputArray = [
      predictionInputs.age,
      predictionInputs.aspect,
      predictionInputs.subscriptions,
      predictionInputs.save_rate,
      predictionInputs.dist_healthy,
      predictionInputs.dist_unhealthy,
      predictionInputs.pop_dense,
      predictionInputs.retail_dense,
      predictionInputs.crime
    ];
    
    // Normalize input using stored parameters
    const inputTensor = tf.tensor2d([inputArray]);
    const normalizedInput = inputTensor.sub(model.normalizationParams.XMean)
                                    .div(model.normalizationParams.XVar.sqrt());
    
    const predictionTensor = model.predict(normalizedInput);
    
    predictionTensor.data().then(result => {
      setPrediction(result[0]);
    });
    
    inputTensor.dispose();
    normalizedInput.dispose();
    predictionTensor.dispose();
  };

  const exportModel = async () => {
    if (!model) return;
    
    try {
      await model.save('downloads://income-prediction-model');
      alert('Model exported successfully!');
    } catch (error) {
      console.error('Export error:', error);
      alert('Export failed. Model saved to browser storage.');
    }
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-white">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4 flex items-center gap-3">
          <Brain className="text-blue-600" />
          Income Prediction with TensorFlow
        </h1>
        <p className="text-gray-600">
          Sequential neural network model to predict income based on demographic and lifestyle factors
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        {/* Model Training Section */}
        <div className="bg-blue-50 p-6 rounded-lg border">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <Settings className="text-blue-600" />
            Model Training
          </h2>
          
          <div className="space-y-4">
            <div className="text-sm text-gray-600">
              Dataset: {csvData ? csvData.length : 0} samples loaded
            </div>
            
            <button
              onClick={trainModel}
              disabled={isTraining || !csvData}
              className="w-full bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50 flex items-center justify-center gap-2"
            >
              <Play size={16} />
              {isTraining ? 'Training...' : 'Train Model'}
            </button>
            
            {modelMetrics && (
              <div className="bg-white p-4 rounded border">
                <h3 className="font-medium mb-2">Model Performance</h3>
                <div className="text-sm space-y-1">
                  <div>RMSE: ${modelMetrics.rmse.toFixed(2)}</div>
                  <div>MAE: ${modelMetrics.mae.toFixed(2)}</div>
                  <div>MSE: {modelMetrics.mse.toFixed(2)}</div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Prediction Section */}
        <div className="bg-green-50 p-6 rounded-lg border">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <BarChart3 className="text-green-600" />
            Make Prediction
          </h2>
          
          <div className="space-y-3">
            {Object.entries(predictionInputs).map(([key, value]) => (
              <div key={key}>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  {key.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                </label>
                <input
                  type="number"
                  step="0.1"
                  value={value}
                  onChange={(e) => setPredictionInputs(prev => ({
                    ...prev,
                    [key]: parseFloat(e.target.value) || 0
                  }))}
                  className="w-full px-3 py-2 border rounded-md text-sm"
                />
              </div>
            ))}
            
            <button
              onClick={makePrediction}
              disabled={!model}
              className="w-full bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 disabled:opacity-50"
            >
              Predict Income
            </button>
            
            {prediction !== null && (
              <div className="bg-white p-4 rounded border text-center">
                <div className="text-sm text-gray-600">Predicted Income</div>
                <div className="text-2xl font-bold text-green-600">
                  ${prediction.toFixed(2)}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Training History */}
      {trainingHistory.length > 0 && (
        <div className="bg-gray-50 p-6 rounded-lg border">
          <h2 className="text-xl font-semibold mb-4">Training Progress</h2>
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 text-sm">
            <div>
              <div className="font-medium">Epoch</div>
              <div>{trainingHistory[trainingHistory.length - 1]?.epoch}</div>
            </div>
            <div>
              <div className="font-medium">Loss</div>
              <div>{trainingHistory[trainingHistory.length - 1]?.loss.toFixed(4)}</div>
            </div>
            <div>
              <div className="font-medium">Val Loss</div>
              <div>{trainingHistory[trainingHistory.length - 1]?.val_loss.toFixed(4)}</div>
            </div>
            <div>
              <div className="font-medium">MAE</div>
              <div>{trainingHistory[trainingHistory.length - 1]?.mae.toFixed(2)}</div>
            </div>
          </div>
        </div>
      )}

      {/* Model Architecture Info */}
      <div className="mt-8 bg-purple-50 p-6 rounded-lg border">
        <h2 className="text-xl font-semibold mb-4">Model Architecture</h2>
        <div className="text-sm space-y-2">
          <div><strong>Input Layer:</strong> 9 features (age, aspect, subscriptions, save_rate, dist_healthy, dist_unhealthy, pop_dense, retail_dense, crime)</div>
          <div><strong>Hidden Layer 1:</strong> 64 neurons, ReLU activation, L2 regularization, 30% dropout</div>
          <div><strong>Hidden Layer 2:</strong> 32 neurons, ReLU activation, L2 regularization, 20% dropout</div>
          <div><strong>Hidden Layer 3:</strong> 16 neurons, ReLU activation</div>
          <div><strong>Output Layer:</strong> 1 neuron, Linear activation (income prediction)</div>
          <div><strong>Optimizer:</strong> Adam (learning rate: 0.001)</div>
          <div><strong>Loss Function:</strong> Mean Squared Error</div>
        </div>
        
        {model && (
          <button
            onClick={exportModel}
            className="mt-4 bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 flex items-center gap-2"
          >
            <Download size={16} />
            Export Model
          </button>
        )}
      </div>
    </div>
  );
};

export default IncomePredictionModel;