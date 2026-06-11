from langchain_classic.tools import tool
@tool
def multiply(a:int,b:int)->int:
    '''
    两数的乘积
    '''
    return a*b
  

print(multiply.name)
print(multiply.description)  
print(multiply.args)   
print(multiply.args_schema.model_json_schema())