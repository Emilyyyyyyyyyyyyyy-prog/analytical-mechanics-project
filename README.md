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

$$\begin{cases}
    \dot{w_1} = w_2 w_3 \Big(\frac{B}{C} - \frac{C}{B} \Big)\\
    \dot{w_2} = w_1 w_3 \Big(\frac{C}{A} - \frac{A}{C} \Big)\\
    \dot{w_3} = w_1 w_2 \Big(\frac{A}{B} - \frac{B}{A} \Big)
  \end{cases}$$

Теперь, расписав уравнение Пуассона, так же выразим производные $q_0, q_1, q_2, q_3$:

$$\Lambda\circ \vec{w} = (q_0 + \vec{q}) \circ \vec{w} = -(\vec{q} \dot \vec{w}) + q_0 \vec{w} + \vec{q} \times \vec{w} = -(q_1w_1 + q_2w_2 + q_3w_3) + q_0 \begin{pmatrix} 
  w_1 \\ 
  w_2 \\ 
  w_3\end{pmatrix} + \begin{pmatrix} 
  q_1 \\ 
  q_2 \\ 
  q_3\end{pmatrix} \times \begin{pmatrix} 
  w_1 \\ 
  w_2 \\ 
  w_3\end{pmatrix}$$

  Скалярное слагаемое правой части - скалярная часть кватерниона $\dot{\Lambda}$, векторная соответствует векторной части. В итоге получим:

  $$\begin{cases}
    \dot{q_0} = -\frac{1}{2}\Big(q_1w_1 + q_2w_2 + q_3w_3)\\
    \dot{q_1} = \frac{1}{2}\Big(q_0w_1 + q_2w_3 - q_3w_2)\\
    \dot{q_2} = \frac{1}{2}\Big(q_0w_2 + q_3w_1 - q_1w_3)\\
    \dot{q_3} = \frac{1}{2}\Big(q_0w_3 + q_1w_2 - q_2w_1)
  \end{cases}$$
