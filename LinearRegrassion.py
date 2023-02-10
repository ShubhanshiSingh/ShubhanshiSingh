{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMFihn+Jkg0Q0xP+XOg7vUu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ShubhanshiSingh/ShubhanshiSingh/blob/main/LinearRegrassion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "C-HhZuZmoi2_"
      },
      "outputs": [],
      "source": [
        "x = [55,58,64,68,70,75,80,84]\n",
        "y = [340,335,410,460,450,610,735,780]\n",
        "i = 0\n",
        "N = len(x)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sum_x = sum(x)\n",
        "sum_y = sum(y)"
      ],
      "metadata": {
        "id": "Ei4gBzthpDuz"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sq_x = [i ** 2 for i in x]"
      ],
      "metadata": {
        "id": "W1kPC-ioqzx5"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x_sq = pow(sum_x,2)"
      ],
      "metadata": {
        "id": "xJ-YXdTFq-Z1"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sum_xy = 0\n",
        "for i in range(0,len(x)):\n",
        "  sum_xy = sum_xy + (x[i] * y[i])"
      ],
      "metadata": {
        "id": "-qrGysgNrWIv"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "prod_xy = sum_x * sum_y"
      ],
      "metadata": {
        "id": "MiRq-c-AtDG7"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"x:\", str(x))\n",
        "print(\"y:\", str(y))\n",
        "print(\"square of x:\", str(sq_x))\n",
        "print(\"x square:\", x_sq)\n",
        "print(\"sum of xy:\", sum_xy)\n",
        "print(\"product of sum of x and y:\", prod_xy)\n",
        "print(N)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GwHo5X78tMw4",
        "outputId": "6717ef83-73ae-48a0-98f6-262fb5e312c0"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "x: [55, 58, 64, 68, 70, 75, 80, 84]\n",
            "y: [340, 335, 410, 460, 450, 610, 735, 780]\n",
            "square of x: [3025, 3364, 4096, 4624, 4900, 5625, 6400, 7056]\n",
            "x square: 306916\n",
            "sum of xy: 297220\n",
            "product of sum of x and y: 2282480\n",
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "w1 = round((sum_xy - (prod_xy/N))/(sum(sq_x)-(x_sq/N)),2)"
      ],
      "metadata": {
        "id": "3AWDz1s0uE--"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "w0 = round((sum_y - (w1 * sum_x))/N, 2)\n",
        "w0 = float(w0)"
      ],
      "metadata": {
        "id": "sPjLrLI8vfJR"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "w0\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2sUCPBwBwAl5",
        "outputId": "23aa171c-6c1c-4cc4-cfd8-b9bb49b036e6"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "-622.09"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from matplotlib import pyplot as plt\n",
        "def plot_regression_line(x,y,w0,w1):\n",
        "  plt.scatter(x, y, color = 'blue', marker = 'o', s = 30)\n",
        "  # print (x)\n",
        "  # print (w1)\n",
        "  y_pred = w0 + w1 * np.array(x)\n",
        "  plt.plot(x, y_pred)\n",
        "  plt.xlabel('x')\n",
        "  plt.ylabel('y')\n",
        "  plt.show()\n",
        "plot_regression_line(x,y,w0,w1)"
      ],
      "metadata": {
        "id": "6uruZkKHwfz4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        },
        "outputId": "496a9ad5-d069-465a-90a4-9f218185d29d"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}