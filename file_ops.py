def read_file(file_name):
    file_contents = " "
    with open(file_name, 'r') as file:
        f = file.readlines()
    for i in f:
        file_contents +=i

    print(file_contents)
    return file_contents
    

def read_file_into_list(file_name):
    lis = []
    with open(file_name, 'r') as file:
        f = file.readline()
        while(f!=""):
            lis.append(f)
            f = file.readline()
    return lis
   

def write_first_line_to_file(file_contents, output_filename):
    print(file_contents)
    file_line = file_contents.split('\n')[0]
    with open(output_filename, 'w') as file:
       file.write(file_line)


def read_even_numbered_lines(file_name):
    lis = [] 
    with open(file_name, 'r') as file: 
        f = file.readlines()
        d = 1   
        for i in f:
            if(d%2==0):
                lis.append(i)
            d+=1
   # res = li[1::2]
    return lis
    


def read_file_in_reverse(file_name):
    lis = []
    with open(file_name, "r") as file:
       for i in file:
           lis.append(i)
            
    res = lis[::-1]
    print(res)
    return res
   
'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
   
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()