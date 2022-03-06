# SR

## 1 项目构建

该项目需要使用`Cython`生成Python扩展模块

```shell
pip install -r requirements.txt
python setup.py build_ext --inplace
```

## 2 实验复现

`SR`输入的是一条kpi曲线，输出经过显著性变换的显著性图和异常分数，将显著性图的每个点的异常分数求和作为该条kpi曲线的异常分数；再结合标注计算best F1-score，pr和roc以及AUC

![image-20220306172520991](https://gitee.com/nk-xiong-xiao/figure-bed/raw/master/img/image-20220306172520991.png)

### 2.1 数据预处理

需要将每台机器的第8天的kpi单独拆出来

```shell
# 在data_yidong目录下
python data_load.py
```

### 2.2 异常片段预测

运行`SR`，对所有机器的kpi曲线进行显著性变换，输出kpi曲线每个点的异常分数，并将每个点的异常分数求和作为整条kpi曲线的异常分数保存到`score_statistics.csv`；参数（窗口大小等）设置见`msanomalydetector/util.py`

```shell
# 在项目根目录下
python main.py > score_statistics.csv
```

### 2.3 实验结果评估

运行`evaluate.ipynb`里的所有代码块即可得到`best F1-score，PR和ROC以及AUC`等实验结果；`roc_evaluate.csv`和`pr_evaluate.csv`分别为绘制ROC和PR曲线所需要的结果

#### 移动数据结果

| item           | result |
| -------------- | ------ |
| best precision | 0.1071 |
| best recall    | 0.5100 |
| best f1        | 0.1771 |
| AUC            | 0.7272 |

