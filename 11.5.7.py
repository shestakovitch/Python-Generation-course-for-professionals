"""Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют
последовательности символов, удовлетворяющие следующим условиям:

последовательность должна состоять только из bee и geek
последовательность должна содержать хотя бы один geek
bee не может находиться рядом с самим собой (не может быть beebee)
geek может появиться только после того, как до этого было записано bee
после каждого bee когда-нибудь должен появиться geek"""

regex = r'(bee(geek)+)+'