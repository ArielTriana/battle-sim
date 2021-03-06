from ..grammar import *
from ..parser.engine_ast import *

eof = Terminal("EOF")

bs_file = NonTerminal("bs_file")
classes = NonTerminal("classes")
statements = NonTerminal("statements")
statement = NonTerminal("statement")
Semicolon = Terminal(";", ";")
func_def = NonTerminal("func_def")
if_def = NonTerminal("if_def")
class_def = NonTerminal("class_def")
while_def = NonTerminal("while_def")
assign = NonTerminal("assign")
return_stat = NonTerminal("return_stat")
_break = Terminal("break", value="break")
_continue = Terminal("continue", value="continue")
expressions = NonTerminal("expressions")
functions = NonTerminal("functions")
constructor = NonTerminal("constructor_def")
tconstructor = Terminal("constructor", "constructor")
attr = NonTerminal("attributes")
attr_def = NonTerminal("attr_def")
_self = Terminal("self", "self")
function = Terminal("function", "function")
name = Terminal("NAME")
lparent = Terminal("(", "(")
rparent = Terminal(")", ")")
arrow = Terminal("->", "->")
_if = Terminal("if", "if")
expression = NonTerminal("expression")
elif_def = NonTerminal("elif_def")
else_def = NonTerminal("else_def")
_elif = Terminal("elif", "elif")
_else = Terminal("else", "else")
_class = Terminal("class", "class")
_is = Terminal("is", "is")
_type = NonTerminal("type")
tnumber = Terminal("number", "number")
oeq = Terminal("=", "=")
_return = Terminal("return", "return")
lcurly = Terminal("{", "{")
rcurly = Terminal("}", "}")
params = NonTerminal("params")
comma = Terminal(",", ",")
disjunction = NonTerminal("disjunction")
_or = Terminal("or", 'or')
conjunction = NonTerminal("conjunction")
_and = Terminal("and", "and")
inversion = NonTerminal("inversion")
_not = Terminal("not", "not")
comparision = NonTerminal("comparision")
_sum = NonTerminal("sum")
_eq = Terminal("eq", "eq")
_neq = Terminal("neq", "neq")
_lte = Terminal("lte", "lte")
_lt = Terminal("lt", "lt")
_gte = Terminal("gte", "gte")
_gt = Terminal("gt", "gt")
plus = Terminal("+", "+")
term = NonTerminal("term")
minus = Terminal("-", "-")
factor = NonTerminal("factor")
mul = Terminal("*", "*")
div = Terminal("/", "/")
mod = Terminal("%", "%")
_pow = NonTerminal("pow")
opow = Terminal("^", "^")
primary = NonTerminal("primary")
dot = Terminal(".", ".")
atom = NonTerminal("atom")
_list = NonTerminal("list")
lbracket = Terminal("[", "[")
rbracket = Terminal("]", "]")
true = Terminal("True")
false = Terminal("False")
none = Terminal("None")
number = Terminal("NUMBER")
_while = Terminal("while", "while")
void = Terminal("void", "void")
_bool = Terminal("bool", "bool")
return_type = NonTerminal("return_type")
decl = NonTerminal("decl")
oand = Terminal("&", "&")
_List = Terminal("List", "List")

bs_file += Production([classes, oand, statements, eof], build_program)
bs_file += Production([eof])

classes += Production([class_def, Semicolon, classes], build_classes1)
classes += Production([class_def, Semicolon], build_classes2)

statements += Production([statement, Semicolon, statements], build_statements1)
statements += Production([statement, Semicolon], build_statements2)

statement += Production([func_def])
statement += Production([if_def])
statement += Production([while_def])
statement += Production([decl])
statement += Production([assign])
statement += Production([return_stat])
statement += Production([_break], build_breack)
statement += Production([_continue], build_continue)
statement += Production([expression])

func_def += Production([function, return_type, name, lparent, params,
                        rparent, arrow, lcurly, statements, rcurly], build_func_def1)
func_def += Production([function, return_type, name, lparent,
                        rparent, arrow, lcurly, statements, rcurly], build_func_def2)

if_def += Production([_if, expression, arrow, lcurly,
                      statements, rcurly, elif_def], build_if_def1)
if_def += Production([_if, expression, arrow, lcurly,
                      statements, rcurly, else_def], build_if_def2)
if_def += Production([_if, expression, arrow, lcurly,
                      statements, rcurly], build_if_def3)

elif_def += Production([_elif, expression, arrow, lcurly,
                        statements, rcurly, elif_def], build_elif_def1)
elif_def += Production([_elif, expression, arrow, lcurly,
                        statements, rcurly, else_def], build_elif_def2)
elif_def += Production([_elif, expression, arrow, lcurly,
                        statements, rcurly], build_elif_def3)

else_def += Production([_else, arrow, lcurly,
                        statements, rcurly], build_else_def)

class_def += Production([_class, name, _is, name, arrow, lcurly,
                         constructor, Semicolon, functions, rcurly], build_class_def1)
class_def += Production([_class, name, _is, name, arrow,
                         lcurly, constructor, Semicolon, rcurly], build_class_def2)

functions += Production([func_def, Semicolon, functions], build_functions1)
functions += Production([func_def, Semicolon],  build_functions2)

constructor += Production([tconstructor, lparent, params,
                           rparent, arrow, lcurly, attr, rcurly], build_constructor1)
constructor += Production([tconstructor, lparent, rparent,
                           arrow, lcurly, attr, rcurly], build_constructor2)
constructor += Production([tconstructor, lparent,
                           rparent, lcurly, rcurly], build_constructor3)

attr += Production([attr_def, Semicolon, attr],  build_attributes1)
attr += Production([attr_def, Semicolon],  build_attributes2)

attr_def += Production([_type, _self, dot, name, oeq,
                        expression], build_attr_def)

while_def += Production([_while, expression, arrow,
                         lcurly, statements, rcurly],  build_while_def)

return_type += Production([void], build_return_type)
return_type += Production([_type], build_return_type)

_type += Production([tnumber],  build_type)
_type += Production([_bool],  build_type)
_type += Production([_List],  build_type)
_type += Production([name], build_type)

decl += Production([_type, name, oeq, expression], build_decl)

assign += Production([name, oeq, expression], build_assign)

return_stat += Production([_return, expression], build_return1)
return_stat += Production([_return], build_return2)

params += Production([_type, name, comma, params],  build_params1)
params += Production([_type, name], build_params2)

expressions += Production([expression, comma, expressions], build_expressions1)
expressions += Production([expression], build_expressions2)

expression += Production([disjunction, _if, disjunction,
                          _else, expression],  build_ternary_expression)
expression += Production([disjunction])

disjunction += Production([conjunction, _or, disjunction], build_disjunction)
disjunction += Production([conjunction])

conjunction += Production([inversion, _and, conjunction], build_conjuction)
conjunction += Production([inversion])

inversion += Production([_not, inversion],  build_inversion)
inversion += Production([comparision])

comparision += Production([_sum, _eq, _sum], build_comparision)
comparision += Production([_sum, _neq, _sum], build_comparision)
comparision += Production([_sum, _lte, _sum], build_comparision)
comparision += Production([_sum, _lt, _sum], build_comparision)
comparision += Production([_sum, _gte, _sum], build_comparision)
comparision += Production([_sum, _gt, _sum], build_comparision)
comparision += Production([_sum])

_sum += Production([_sum, plus, term], build_aritmetic_expression)
_sum += Production([_sum, minus, term], build_aritmetic_expression)
_sum += Production([term])

term += Production([term, mul, factor], build_aritmetic_expression)
term += Production([term, div, factor], build_aritmetic_expression)
term += Production([term, mod, factor], build_aritmetic_expression)
term += Production([factor])

factor += Production([plus, factor])
factor += Production([minus, factor])
factor += Production([_pow])

_pow += Production([primary, opow, factor], build_aritmetic_expression)
_pow += Production([primary])

primary += Production([primary, dot, name], build_primary1)
primary += Production([primary, lparent, expressions, rparent], build_primary2)
primary += Production([primary, lparent, rparent],  build_primary3)
primary += Production([_self,dot,name],build_primary4)
primary += Production([atom])
primary += Production([lparent,expression,rparent],build_pexpression)

atom += Production([name], build_Variable)
atom += Production([true],  build_Bool)
atom += Production([false], build_Bool)
atom += Production([none], build_None)
atom += Production([number], build_Number)
atom += Production([_list])

_list += Production([lbracket, expressions, rbracket], build_list1)
_list += Production([lbracket, rbracket], build_list2)


GRAMMAR = Grammar(bs_file)
