####################################################
# Match for python 3.10
serie = "N-01"
match serie:
    case "N-01":
        print("N-01")
    case "N-02":
        print("N-02")
    case "N-03":
        print("N-03")
    case _:
        print("default")

client ={'name':'John','age':25,'country':'USA'}
movie ={'name':'John Wick','data_sheet':{'protagonist':'Keanu Reeves','director':'Quentin Tarantino'}}

elements = [client, movie, 'book']

for e in elements:
    match e:
        case {'name':name,'age':age,'country':country}:
            print('it is a client')
            print(f'name is {name} and age is {age} and country is {country}')
        case {'name':name,'data_sheet':{'protagonist':protagonist,'director':director}}:
            print('it is a movie')
            print(f'name is {name} and director is {director} and protagonist is {protagonist}')
        case _:
            print('it is a book')