from PDF_Reader import read_PDF

def getGPA(file_name):
    text=read_PDF(file_name)
    for char in range(len(text)):
        if(text[char]=='3' or  text[char]=='2' or text[char]=='1' or text[char]=='4'):
            if(text[char+1]=='.'):
                print("POSSIBLE GPA: ", text[char:char+4])
    print("PDF searched")

#important, when calling a path from python, call it from the root directory fo your project!
getGPA("3_HypeAI/LIN_XINLEI_Short_Resume (english version).pdf")