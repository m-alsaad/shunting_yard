import unittest
import shunting_yard as sy


class TokenizeTest(unittest.TestCase):

	"""Simple Example on how Unit Test works"""
	def test_single_operator(self):
		tokens = list(sy.tokenize('1+2'))
		self.assertListEqual(tokens, ['1', '+', '2'])


	def test_infixToPostfix(self):
		self.assertEqual(sy.infixToPostfix('1+1'), '1 1 +')
		self.assertEqual(sy.infixToPostfix('1'), '1')
		self.assertEqual(sy.infixToPostfix('+'), '+')
		self.assertEqual(sy.infixToPostfix('((5+5)*2+3-5)/3'), '5 5 + 2 * 3 + 5 - 3 /')


	def test_isDigit(self):
		self.assertEqual(sy.isDigit('1'), True)
		self.assertEqual(sy.isDigit('a'), False)
		self.assertEqual(sy.isDigit('$'), False)
		self.assertEqual(sy.isDigit('='), False)
		self.assertEqual(sy.isDigit('™'), False)
		self.assertEqual(sy.isDigit('🤡'), False)


	def test_isLeftBracket(self):
		self.assertEqual(sy.isLeftBracket('['), True)
		self.assertEqual(sy.isLeftBracket('1'), False)
		self.assertEqual(sy.isLeftBracket('a'), False)
		self.assertEqual(sy.isLeftBracket('$'), False)
		self.assertEqual(sy.isLeftBracket('='), False)
		self.assertEqual(sy.isLeftBracket('™'), False)
		self.assertEqual(sy.isLeftBracket('🤡'), False)


	def test_isRightBracket(self):
		self.assertEqual(sy.isRightBracket(']'), True)
		self.assertEqual(sy.isRightBracket('1'), False)
		self.assertEqual(sy.isRightBracket('a'), False)
		self.assertEqual(sy.isRightBracket('$'), False)
		self.assertEqual(sy.isRightBracket('='), False)
		self.assertEqual(sy.isRightBracket('™'), False)
		self.assertEqual(sy.isRightBracket('🤡'), False)


	def test_isNumber(self):
		self.assertEqual(sy.isNumber(['1']), True)
		self.assertEqual(sy.isNumber(['1', '2']), True)
		self.assertEqual(sy.isNumber(['a']), False)
		self.assertEqual(sy.isNumber(['$']), False)
		self.assertEqual(sy.isNumber(['=']), False)
		self.assertEqual(sy.isNumber(['™']), False)
		self.assertEqual(sy.isNumber(['🤡']), False)


	def test_isOperator(self):
		self.assertEqual(sy.isOperator('+'), True)
		self.assertEqual(sy.isOperator('-'), True)
		self.assertEqual(sy.isOperator('*'), True)
		self.assertEqual(sy.isOperator('/'), True)
		self.assertEqual(sy.isOperator('1'), False)
		self.assertEqual(sy.isOperator('a'), False)
		self.assertEqual(sy.isOperator('$'), False)
		self.assertEqual(sy.isOperator('='), False)
		self.assertEqual(sy.isOperator('™'), False)
		self.assertEqual(sy.isOperator('🤡'), False)


	def test_peekAtStack(self):
		self.assertEqual(sy.peekAtStack(['1']), '1')
		self.assertEqual(sy.peekAtStack(['1', '2']), '1')
		self.assertEqual(sy.peekAtStack(['a', '2']), 'a')
		self.assertEqual(sy.peekAtStack(['+']), '+')


	def test_popFromStack(self):
		self.assertEqual(sy.popFromStack(['1']), '1')
		self.assertEqual(sy.popFromStack(['a']), 'a')
		self.assertEqual(sy.popFromStack(['1', '2']), '1')
		self.assertEqual(sy.popFromStack(['a', '2']), 'a')


	""" THIS FUNCTION DOES NOT HAVE A RETURN!
    
	def test_pushToStack(self):
		stack = ['1']
		self.assertEqual(sy.pushToStack(stack, '2')...)
	"""

	def test_stackIsEmpty(self):
		self.assertEqual(sy.stackIsEmpty([]), True)
		self.assertEqual(sy.stackIsEmpty(['1']), False)
		self.assertEqual(sy.stackIsEmpty(['1', '2']), False)
		self.assertEqual(sy.stackIsEmpty(['a']), False)
		self.assertEqual(sy.stackIsEmpty(['$']), False)
		self.assertEqual(sy.stackIsEmpty(['™']), False)
		self.assertEqual(sy.stackIsEmpty(['🤡']), False)
