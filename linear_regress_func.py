def linear_regress(x : list , y : list) -> tuple[ float , float ]:
	learning_rate = 0.001

	m = 0.0

	b = 0.0

	for epoch in range(10000):

		dm = 0

		db = 0

		for i in range(len(x)):
			y_pred = m * x[i] + b #using straight line formula y = mx + b
			error = y_pred - y[i]

			dm -= x[i] * error

			db -= error

		m += learning_rate * (1/len(x)) * dm
		b += learning_rate * (1/len(x)) * db

		return m , b

	print(f"Predicted value of m: {m} \n Predicted value of b: {b}");
