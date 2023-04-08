import { d3, useEffect } from "../mod.ts";
import { BarChartProps } from "../chart-props/BarChartProps.ts";
import { Button } from "../../components/Button.tsx";

// need to work on paddings that dynamically update to avoid overlapping with the graph

export default function BarChartShort(props: BarChartProps) {
  const yLabelPadding = 20;
  const xLabelPadding = 20;
  const padding = {
    top: (props.paddingTop || 50) + yLabelPadding,
    right: (props.paddingRight || 50) + xLabelPadding,
    bottom: (props.paddingBottom || 50) + yLabelPadding,
    left: (props.paddingLeft || 50) + xLabelPadding,
  };
  const width = (props.width || 800) - padding.left - padding.right -
    yLabelPadding * 2;
  const height = (props.height || 600) - padding.bottom - padding.top -
    xLabelPadding * 2;
  const barPadding = 3; // padding provided between each bar
  const animation = props.animation == false ? props.animation : true;
  const animationDuration = props.animationDuration || 800;
  const animationDelay = props.animationDelay || 100;
  const barHoverColor = props.barHoverColor || "#90BE6D";
  const fontFamily = props.fontFamily || "Verdana";
  const axesColor = props.axesColor || "#4D908E";
  const font_size = "1.5em"; // .style("font", "14px times")

  let datasets: {
    label:
      | string
      | number
      | boolean
      | d3.ValueFn<SVGTextElement, any, string | number | boolean | null>
      | null;
  }[] = []; // cleaned datasets are stored here

  let drawPoints: any[] = [];

  function cleanDatasets() { //cleans data sets by reading from receivedDatasets
    const receivedDatasets = props.datasets || [];
    datasets = [];
    drawPoints = [];
    for (let ds of receivedDatasets) {
      const tempData = [];
      for (let obj of ds.data) {
        const values = Object.values(obj);
        tempData.push({
          x: values[1],
          y: values[0],
        });
      }
      datasets.push({
        label: ds.label,
        color: ds.color,
        data: tempData,
      });
      drawPoints = [...drawPoints, ...tempData];
    }
  }

  let xScale:
    | d3.ScaleBand<string>
    | d3.AxisScale<d3.AxisDomain>
    | null = null;
  let yScale:
    | d3.ScaleLinear<number, number, never>
    | d3.AxisScale<d3.AxisDomain>
    | { (arg0: any): number; invert: (arg0: any) => number }
    | null = null;

  function configureScale() {
    const labels: any[] | Iterable<string> = [];
    datasets[0].data.forEach((name: { x: any }) => {
      labels.push(name.x);
    });

    xScale = d3.scaleBand()
      .domain(labels)
      .range([0, width]);

    const maxObj = drawPoints.reduce((obj1, obj2) => {
      return obj1.y > obj2.y ? obj1 : obj2;
    });
    const minObj = drawPoints.reduce((obj1, obj2) => {
      return obj1.y < obj2.y ? obj1 : obj2;
    });
    const moy = maxObj.y;
    console.log("maxObj.y=" + JSON.stringify(moy, null, 4));

    // printDebug("configureScale() before");
    yScale = d3.scaleLinear()
      .domain([0, maxObj.y])
      .range([height, 0]);
    // yScale = d3.scaleLinear().domain([0, 20]).range([height, 0]);
    // printDebug("configureScale() after");
  }

  function updateChart() {
    d3.select(".bar-chart")
      .attr("width", width + padding.left + padding.right + 2 * yLabelPadding)
      .attr(
        "height",
        height + padding.top + padding.bottom + 2 * xLabelPadding,
      );

    const yAxis = d3.axisLeft(yScale);
    const xAxis = d3.axisBottom(xScale);
    yAxis.tickSizeOuter(0);
    xAxis.tickSizeOuter(0);

    // update with width / datasets.length;

    const paddingBarGroup = 10;
    const barContainer = width / datasets[0].data.length - paddingBarGroup;
    const barWidth = barContainer / datasets.length;
    // idea is to group chart of specific group into one area and then provide spacing for the other grouped chart
    for (let i = 0; i < datasets[0].data.length; i++) {
      // append g first
      const currGroup = d3
        .select(".bars")
        .append("g")
        .attr("x", paddingBarGroup * i);
      for (let j = 0; j < datasets.length; j++) {
        currGroup
          .append("rect")
          .attr("x", function (): number {
            return (
              Number(currGroup.node()?.getAttribute("x")) +
              barWidth * i * datasets.length +
              barWidth * j +
              yLabelPadding +
              padding.left +
              paddingBarGroup / 2
            );
          })
          .attr("width", barWidth)
          .attr("height", 0)
          .attr("y", height + padding.top + yLabelPadding - barPadding)
          .transition()
          .ease(d3.easeCubic)
          .delay(function (): number {
            return i * animationDelay * (animation ? 1 : 0);
          })
          .duration(animationDuration * (animation ? 1 : 0))
          .attr("y", function (): number {
            return (
              yScale(datasets[j].data[i].y) +
              padding.top +
              yLabelPadding -
              barPadding
            );
          })
          .attr("height", function (): number {
            return height - yScale(datasets[j].data[i].y);
          })
          .attr("stroke-width", 1)
          .attr("stroke", barHoverColor)
          .attr("rx", "3")
          .attr("fill", datasets[j].color);

        //console.log("currGroup=" + JSON.stringify(currGroup, null, 4));
      }
    }

    const barChart = d3.select(".bar-chart");

    // render y Axis
    barChart
      .insert("g", "g")
      .call(yAxis)
      // have to make this data to show for charts dynamic
      .attr(
        "transform",
        `translate(${padding.left + yLabelPadding}, ${
          padding.top + xLabelPadding
        })`,
      )
      // .attr("font-size", "0.5em")
      .attr("font-size", font_size)
      .attr("font-family", fontFamily)
      .attr("color", axesColor)
      .selectAll(".tick line")
      .attr("x2", width)
      .attr("stroke-width", "0.5")
      .attr("opacity", "0.3");

    // render x Axis
    barChart
      .insert("g", "g")
      .call(xAxis)
      .attr(
        "transform",
        `translate(${padding.left + yLabelPadding}, ${
          height + padding.bottom + xLabelPadding
        })`,
      )
      .attr("font-size", font_size)
      .attr("font-family", fontFamily)
      .attr("color", axesColor)
      .selectAll(".tick line")
      .attr("stroke-width", "0.5")
      .attr("opacity", "0.3")
      .attr("y2", -height);
  }

  useEffect(() => {
    console.log("useEffect called in BarChart.tsx");
    // console.log("props=" + JSON.stringify(props, null, 4));

    cleanDatasets();

    configureScale();

    updateChart();
  }, []);

  let myxaxis: d3.Selection<d3.BaseType, unknown, SVGGElement, unknown>;

  function updateChartShort() {
    d3.select(".bar-chart")
      .attr("width", width + padding.left + padding.right + 2 * yLabelPadding)
      .attr(
        "height",
        height + padding.top + padding.bottom + 2 * xLabelPadding,
      );
    // console.log("yScale=" + JSON.stringify(yScale, null, 4));

    const yAxis = d3.axisLeft(yScale);
    const xAxis = d3.axisBottom(xScale);
    yAxis.tickSizeOuter(0);
    xAxis.tickSizeOuter(0);

    // update with width / datasets.length;

    const paddingBarGroup = 10;
    const barContainer = width / datasets[0].data.length - paddingBarGroup;
    const barWidth = barContainer / datasets.length;
    // idea is to group chart of specific group into one area and then provide spacing for the other grouped chart
    for (let i = 0; i < datasets[0].data.length; i++) {
      // append g first
      const currGroup = d3
        .select(".bars")
        .append("g")
        .attr("x", paddingBarGroup * i);
      for (let j = 0; j < datasets.length; j++) {
        currGroup
          .append("rect")
          .attr("x", function (): number {
            return (
              Number(currGroup.node()?.getAttribute("x")) +
              barWidth * i * datasets.length +
              barWidth * j +
              yLabelPadding +
              padding.left +
              paddingBarGroup / 2
            );
          })
          .attr("width", barWidth)
          .attr("height", 0)
          .attr("y", height + padding.top + yLabelPadding - barPadding)
          .transition()
          .ease(d3.easeCubic)
          .delay(function (): number {
            return i * animationDelay * (animation ? 1 : 0);
          })
          .duration(animationDuration * (animation ? 1 : 0))
          .attr("y", function (): number {
            return (
              yScale(datasets[j].data[i].y) +
              padding.top +
              yLabelPadding -
              barPadding
            );
          })
          .attr("height", function (): number {
            return height - yScale(datasets[j].data[i].y);
          })
          .attr("stroke-width", 1)
          .attr("stroke", barHoverColor)
          .attr("rx", "3")
          .attr("fill", datasets[j].color);

        // console.log("currGroup=" + JSON.stringify(currGroup, null, 4));
      }
    }

    const barChart = d3.select(".bar-chart");
    // svg.selectAll("g.x.axis")
    //     .call(xAxis);

    // render y Axis
    // barChart
    //   .insert("g", "g")
    //   .call(yAxis)
    //   // have to make this data to show for charts dynamic
    //   .attr(
    //     "transform",
    //     `translate(${padding.left + yLabelPadding}, ${
    //       padding.top + xLabelPadding
    //     })`,
    //   )
    //   .attr("font-size", font_size)
    //   .attr("font-family", fontFamily)
    //   .attr("color", axesColor)
    //   .selectAll(".tick line")
    //   .attr("x2", width)
    //   .attr("stroke-width", "0.5")
    //   .attr("opacity", "0.3");

    // render x Axis
    myxaxis = barChart
      .insert("g", "g")
      .call(xAxis)
      .attr(
        "transform",
        `translate(${padding.left + yLabelPadding}, ${
          height + padding.bottom + xLabelPadding
        })`,
      )
      .attr("font-size", font_size)
      .attr("font-family", fontFamily)
      .attr("color", axesColor)
      .selectAll(".tick line")
      .attr("stroke-width", "0.5")
      .attr("opacity", "0.3")
      .attr("y2", -height);
  }

  useEffect(() => {
    console.log("useEffect short update");
    // console.log("props=" + JSON.stringify(props, null, 4));
    cleanDatasets();

    printDebug("useEffect() before configureScale()");
    configureScale();
    printDebug("useEffect() after configureScale()");

    // console.log("yScale=" + JSON.stringify(yScale, null, 4));

    updateChartShort();
  }, [props.passedDown]);

  function printDebug(calledFrom: string) {
    if (yScale) {
      console.log(
        calledFrom + " yScale(1)=" + JSON.stringify(yScale(1), null, 4),
      );
    } else {
      console.log(calledFrom + " yScale does not exist");
    }
  }

  const changeData = () => {
    console.log("changeData called");
    // console.log("datasets before" + JSON.stringify(datasets, null, 4));
    // datasets1[0].data[0] = {
    //   y: 8,
    //   x: "x1",
    // };
    // setData(datasets1);
    // console.log("datasets after" + JSON.stringify(datasets, null, 4));
    // setTest("changed");
    // titleOnOff = false;

    d3.select(".y.axis").append("g").remove();

    d3.selectAll("g.y.axis").remove();

    d3.selectAll(".bars").append("g").remove();

    // these work:
    d3.select(".bars").remove(); // removes all 'g' elements from the DOM.
    // d3.selectAll('g').remove(); // removes all 'g' elements from the DOM.
    // d3.selectAll(".bars").remove(); // removes all 'g' elements from the DOM.
    // d3.selectAll('.bar-chart').remove(); // removes all 'g' elements from the DOM.
  };

  return (
    <>
      {props.passedDown}
      {width}
      <div className="chart-container">
        <svg className="bar-chart">
          <g>
            <g className="bars"></g>
          </g>
        </svg>
        <Button onClick={changeData}>change Data</Button>
      </div>
    </>
  );
}
