# -*- coding: UTF-8 -*-

import sys
import subprocess #импорт модуля запуска сторонних программ
import argparse #импорт модуля работы с аргументами

#текст для преобразования
testText = "AS as fd \nsddda aaa\nwqqq wwww qq qqq"
#контрольный текст
controlText = "AS\tas\tfd\t\nsddda\taaa\nwqqq\twwww\tqq\tqqq"
#команда на вызов тестируемого проекта
cmd = "dotnet run --project "


#парсим аргументы
def CreateParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--project', required=True)
    parser.add_argument('-t', '--testfile', required=True)
    return parser

#пишем в тестовый файл текст для преобразования
def WriteToFile(filePath, text):
    testFile = open(filePath,"w")
    testFile.writelines(text)

#считываем из преобразованного файла текст и сверяем с эталоном
def ControlRead(filePath, controlText):
    controlFile = open(filePath, "r")
    tmpText = controlFile.readlines()
    return tmpText == controlText


if __name__ == "__main__":

    parser = CreateParser()
    namespace = parser.parse_args(sys.argv[1:])
    testFilePath = namespace.testfile
    pathToProject = namespace.project
    
    WriteToFile(testFilePath , testText)

    #subprocess.run()

    testPassed = ControlRead(testFilePath, controlText)
    print(testPassed)