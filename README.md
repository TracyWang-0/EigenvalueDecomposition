## 数值与符号计算实验之特征值分解
### 一、实验目标
#### 1. 实现下面五个函数
```C++
// 1) 用幂法求矩阵的最大特征值及其特征向量
bool power_eng(double* pld, double* env, double* a, int n);

// 2) 用反幂法求矩阵的最小特征值及其特征向量
bool inv_power_eng(double* pld, double* env, double* a, int n);

// 3) 用Jacobi方法求对称矩阵的全部特征值
bool jacobi_eng(double* ev, double* a, int n);

// 4) 用Gauss相似变换将矩阵就地转换为上Hessenberg矩阵
void gauss_hessen(double* a, int n);

// 5) 矩阵特征值问题QR算法辅助函数
bool qr_aux(int i, int j);
```
#### 2. 求以下四个矩阵A、B、C、D的特征值
![矩阵A](https://user-images.githubusercontent.com/68034401/121653850-b3e36f80-cacf-11eb-8e0a-f67111859858.png)

![矩阵B](https://user-images.githubusercontent.com/68034401/121653879-b9d95080-cacf-11eb-9f2c-e5db38a5c35b.png)

![矩阵C](https://user-images.githubusercontent.com/68034401/121653929-c52c7c00-cacf-11eb-8e8c-bc8ecdc270fa.png)

![矩阵D](https://user-images.githubusercontent.com/68034401/121653942-c9f13000-cacf-11eb-813f-0dc91eff85f2.png)

### 二、代码逻辑
#### 1. matrix.py
    初始化4个矩阵
#### 2. method.py
    实现5个函数
