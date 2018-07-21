from PIL import Image





fileOpen = input("Name of file: ")
fileLoad = input("Name of text file: ")
orientation = input("What`s orientation(normal|90○ left)? Enter 1 or 2 ")





image = Image.open('photos/'+fileOpen)
width = image.size[0]  
height = image.size[1] 	
pix = image.load() #Выгружаем значения пикселей.

variants = ["♦", "#", "$", "&", "N", "%", "M", "H", "P", "K", \
        "Z", "T", "?", "/", ":", "."]
#variants = ["◘","♦", "#", "$", "&", "N", "%", "M", "H", "P", "K", \
 #       "Z", "T", "?", "/", ":", ".", " "]   # Try more elements


files = {}

def doByI(i):
  print('function started')
  global files
  for j in range(height):
      a = pix[i, j][0]
      b = pix[i, j][1]
      c = pix[i, j][2]
      S = (a + b + c) // 3
      number = int(S // len(variants))
      files[(i, j)] = variants[number]
  if i == width - 1:
    return files
      
def main():
  global files
  List = list(range(width))
  print('map activated')
  for i in List:
    doByI(i)
  print('map end')
  a = files
  print(a)
  print(len(a))
  input("Press the button, please")
  with open(fileLoad, "w") as file:
    pass
  ForFile = ""
  allOf = width * height
  if orientation == "1":
    for j in range(height):
      ForFile += "\n"
      for i in range(width):
        print(j * width + i, '/', allOf, str(int((j * width + i) / allOf * 100)) + "%")
        ForFile += a[(i, j)]
        print(a[(i, j)])
      if len(ForFile) >= 1000:
          with open(fileLoad, "a", encoding = "utf-8") as file:  
              file.write(ForFile)
              ForFile = ""
  elif orientation == "2":
    for i in range(width):
      ForFile += "\n"
      for j in range(height):
        print(i * height + j, '/', allOf, str(int((i * height + j) / allOf * 100)) + "%")
        ForFile += a[(i, j)]
        print(a[(i, j)])
      if len(ForFile) >= 1000:
          with open(fileLoad, "a", encoding = "utf-8") as file:  
              file.write(ForFile)
              ForFile = ""
  else:
    print("Your orientation is not defined.")
  print('End')

    

if __name__ == "__main__":
  main()

