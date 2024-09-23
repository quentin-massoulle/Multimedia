import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,50)
p = 2
q = 0.1

y = p*np.exp(q*x)

# Calcul de p et q en utilisants tous les points
A = np.column_stack((np.ones(len(x)), x))
B = np.array(np.log(y))

At = np.transpose(A)
X = np.linalg.inv(At @ A) @ At @ B
p_est = np.exp(X[0])
q_est = X[1]
y_est = p_est*np.exp(q_est*x)


#on fait pareil en utilisant les valeurs bruités
yb = y + np.random.normal(-0.2,0.2,len(x))
B= np.array(np.log(yb))
X_br = np.linalg.inv(At@A) @ At @ B
p_br_est = np.exp(X_br[0])
q_br_est = X_br[1]

y=y+5



y_br_est = p_br_est*np.exp(q_br_est*x)

somme_y  = np.sum(np.sqrt(np.pow((x-y), 2)))
somme_y_br =np.sum(np.sqrt(np.pow((x-y_br_est), 2)))
somme_yb = np.sum(np.sqrt(np.pow((x-yb), 2)))

diff_y = np.abs(somme_y - somme_y_br)
diff_yb = np.abs(somme_yb - somme_y_br)

if (diff_y>diff_yb):
    plt.plot(x, y_br_est, 'r')
else:
    plt.plot(x,y,'b')


plt.plot(x, yb, 'og')

plt.show()