{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "digraph {\n",
      "\tgraph [rankdir=LR]\n",
      "\ta [label=\"{ type | data 3.0000 | grad 4.0000 }\" shape=record]\n",
      "\tb [label=\"{ type | data 3.0000 | grad 4.0000 }\" shape=record]\n",
      "\ta -> b\n",
      "}\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'abcd.gv.jpg'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/snap/core20/current/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /lib/x86_64-linux-gnu/libproxy.so.1)\n",
      "Failed to load module: /home/tmeng12/snap/code/common/.cache/gio-modules/libgiolibproxy.so\n",
      "eog: symbol lookup error: /snap/core20/current/lib/x86_64-linux-gnu/libpthread.so.0: undefined symbol: __libc_pthread_init, version GLIBC_PRIVATE\n"
     ]
    }
   ],
   "source": [
    "from graphviz import Source\n",
    "\n",
    "path = 'abcd.dot'\n",
    "s = Source.from_file(path)\n",
    "print(s.source)\n",
    "\n",
    "s.render('abcd.gv', format='jpg',view=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
