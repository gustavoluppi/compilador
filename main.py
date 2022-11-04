from constants import STATES, ALL_ELEMENTS, BIN_OPS , OPERATORS
import re
import methods

flag=0
line = 0
column = 0
estado = STATES.INITIAL
answer = []
token = ""
numeric_token = ""
comment = ""

def addId(token):
    tipo = OPERATORS.get(token)
    if tipo is not None:
        answer.append([tipo, token])
    elif re.match(r"[\d]", token):
        answer.append(["NUMBER",token])
    else:
        answer.append(["ID", token])

def addId_double(token):
    global flag
    if re.match(r"[\=]", token) and curr_line[column] == "=" :
        
        flag = 1
        addId("==")
        elem = curr_line[column]
    
    elif re.match(r"[\<]", token) and curr_line[column] == "=" :
        flag = 1
        addId("<=")
        elem = curr_line[column]
    
    elif re.match(r"[\>]", token) and curr_line[column] == "=" :
        flag = 1
        addId(">=")
        elem = curr_line[column]
    
    elif re.match(r"[\&]", token) and curr_line[column] == "&" :
        flag = 1
        addId("&&")
        elem = curr_line[column]
    
    elif re.match(r"[\|]", token) and curr_line[column] == "|" :
        flag = 1
        addId("||")
        elem = curr_line[column]

    elif re.match(r"[\!]", token) and curr_line[column] == "=" :
        flag = 1
        addId("!=")
        elem = curr_line[column]
                        
    else:
      
        
        addId(token)
        


def addError(token):
    if token != "\n" and token != " ":
        answer.append(["Token não existe", token])



input_file = open("example.c", "r")

if __name__ == '__main__':

    for curr_line in input_file:
        line = line + 1
        column = 0
        for elem in curr_line:
            column = column + 1
            if flag == 1:
                flag = 0
                continue


            if estado == STATES.INITIAL: 
                if elem == "/" and curr_line[column] == "*" and estado == STATES.INITIAL and estado != STATES.COMMENT:
                    estado = STATES.COMMENT
                    addId("/*")

                if re.search(r"^(#)", curr_line) and estado == STATES.INITIAL and estado != STATES.COMMENT:
                    break

                if re.search(r"([A-Za-z_])", elem) and estado == STATES.INITIAL and estado != STATES.COMMENT:
                    estado = STATES.IDENTIFIER

                if re.match(r"[0-9]", elem) and estado == STATES.INITIAL and estado != STATES.COMMENT:
                    estado = STATES.NUMERIC
                if re.match(r"[\"]", elem) and estado == STATES.INITIAL and estado != STATES.COMMENT:
                    estado = STATES.LITERAL                                
                if methods.is_number(elem) and methods.is_special_caracter(elem) and estado == STATES.INITIAL and estado != STATES.COMMENT:                                       
                    if not methods.is_error(elem):                                              
                        addId_double(elem)
                        if flag == 1:
                            continue                        
                        
                    else:                       
                        if elem == '&' and curr_line[column] == "&":
                            addId_double(elem)                        
                        elif elem == '|' and curr_line[column] == "|":
                            addId_double(elem)                        
                        elif elem == "!" and curr_line[column] == "=":
                            addId_double(elem)                       
                        else:                           
                            addError(elem)
            
            


            if estado == STATES.COMMENT:
                comment = comment + elem
                if re.search(r"(\*\/)", comment):
                    estado = STATES.INITIAL
                    addId("*/")
                    
            if estado == STATES.NUMERIC: 
                if re.match(r"[\w.]", elem):
                    numeric_token = numeric_token + elem
                if methods.is_number(elem):
                    if re.match(r"(^[0-9]*$)", numeric_token):
                        if re.match(r"(^[0-9]*$)", numeric_token) is not None:
                            addId(numeric_token)
                            if elem != " ":
                                if not methods.is_error(elem):
                                    addId_double(elem)     
                                else:
                                    addError(elem)
                            estado = STATES.INITIAL
                            numeric_token = ""
                    else:
                        if elem in ALL_ELEMENTS or re.match(r"\s|\n", elem) or elem in BIN_OPS:
                            addError(elem)
                            numeric_token = ""
                            estado = STATES.INITIAL
                else:
                    if methods.is_number(elem):
                        if elem != " ":
                            if not methods.is_error(elem):
                                
                                addId_double(elem)
                            else:
                                addError(elem)
                        estado = STATES.INITIAL


            if estado == STATES.IDENTIFIER:                
                if re.match(r"([\w])", elem):
                    token = token + elem                    
                if methods.is_special_caracter(elem):
                    estado = STATES.INITIAL                  
                    if methods.is_reserved_word(token):                        
                        addId(token)
                        if elem != " ":
                            if not methods.is_error(token):                                                            
                                addId_double(elem)                                     
                            else:
                                addError(token)
                        token = ""
                    else:          
                        addId(token)
                        if methods.is_special_caracter(elem):
                            if elem != re.match(r"\s", elem):
                                if not methods.is_error(elem):  
                                    addId_double(elem)    
                                else:
                                    if elem == "!" and curr_line[column] == "=":
                                        addId_double(elem)
                                    else:
                                        addError(elem)
                            estado = STATES.INITIAL
                        token = ""

            if estado == STATES.LITERAL:  
                if re.match(r"[%a-zA-z0-9\"\s]", elem):
                    token = token + elem
                if re.match(r"[\"]", elem):
                    lit = re.match(r"[\"]+[%\w\s]+[\"]*", token)
                    if lit is not None:
                        addId(lit.group())
                        token = ""
                        estado = STATES.INITIAL



            




    print(answer)
