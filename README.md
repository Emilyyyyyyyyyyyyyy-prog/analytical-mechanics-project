## Проект по аналитической механике
-- модель движения твердого тела --

### 1. Теоретические расчеты
Для модели потребуются две основные формулы:
* динамическая формула Эйлера: $I_0 \dot{\vec{w}} + \vec{w} \times I_0 \vec{w} = M_0^{ex}$, для нашей системы $M_0^{ex} = 0$
* кинематическая формула Пуассона: $\dot{\Lambda} = \frac{1}{2} \Lambda\circ\vec{w}$

Запишем тензор инерции в главных осях инерции:

$$I_0 = \begin{pmatrix}
  A & 0 & 0 \\
  0 & B & 0 \\
  0 & 0 & C \end{pmatrix}$$

Выразим и распишем в координатах $\dot{\vec{w}}$:

$$\begin{pmatrix}
  \dot{w_1} \\
  \dot{w_2} \\
  \dot{w_3} \end{pmatrix} = -I_0^{-1}\vec{w}\times I_0\vec{w} = - \begin{pmatrix}
  \frac{1}{A} & 0 & 0 \\
  0 & \frac{1}{B} & 0 \\
  0 & 0 & \frac{1}{C} \end{pmatrix} \begin{pmatrix} 
  w_1 \\ 
  w_2 \\ 
  w_3\end{pmatrix} \times \begin{pmatrix}
  A & 0 & 0 \\
  0 & B & 0 \\
  0 & 0 & C \end{pmatrix} \begin{pmatrix}  
  w_1 \\ 
  w_2 \\ 
  w_3\end{pmatrix} = -\begin{pmatrix}  
  \frac{w_1}{A} \\ 
  \frac{w_2}{B} \\ 
  \frac{w_3}{C}\end{pmatrix} \times \begin{pmatrix}  
  w_1 \dot A \\ 
  w_2 \dot B\\ 
  w_3 \dot C\end{pmatrix} = -\begin{pmatrix}  
  w_2 w_3 \Big(\frac{B}{C} - \frac{C}{B} \Big) \\ 
  w_1 w_2 \Big(\frac{C}{A} - \frac{A}{c} \Big) \\ 
  w_1 w_2 \Big(\frac{A}{B} - \frac{B}{A} \Big)\end{pmatrix}$$

В итоге получаем:

