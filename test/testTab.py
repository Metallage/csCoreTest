# -*- coding: UTF-8 -*-

import sys
import subprocess #импорт модуля запуска сторонних программ
import argparse #импорт модуля работы с аргументами

#текст для преобразования
testText = 'AS as\nza za \n112 332'
#контрольный текст
controlText = 'AS\tas\nza\tza\t\n112\t332'
#команда на вызов тестируемого проекта
cmd = ["dotnet", "run", "--project"]


#парсим аргументы
def CreateParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--project', required=True)
    parser.add_argument('-t', '--testfile', required=True)
    return parser

#пишем в тестовый файл текст для преобразования
def WriteToFile(filePath, text):
    testFile = open(filePath,"w")
    testFile.write(text)

#считываем из преобразованного файла текст и сверяем с эталоном
def ControlRead(filePath, controlText):
    controlFile = open(filePath, "r")
    tmpText = controlFile.read()
    return tmpText == controlText

#точка входа в скрипт
if __name__ == "__main__":

    #тут распарсиваем входные параметры
    parser = CreateParser()
    namespace = parser.parse_args(sys.argv[1:])
    testFilePath = namespace.testfile
    pathToProject = namespace.project
    
    #пишем тестовый файл и передаём его тестируемому приложению
    WriteToFile(testFilePath , testText)
    cmd +=[pathToProject, testFilePath]
    process = subprocess.Popen(cmd)
    process.wait()

    #проверяем результат
    testPassed = ControlRead(testFilePath, controlText)
    if testPassed:
        print("Test passed")
    else:
        print("Test FAILED!!!")
    
