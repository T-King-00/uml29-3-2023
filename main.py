



###pipeline
"""
format of user story . As a ..... , i want to , so that   ...... .
0-getting file
1-file preproccessing (detection of line rules . starting of
    sentence is as and middle word i want to ,so that and full stop .((not done yet))
2-sentence separation . ()
3-class entities        ()
4-class atributes ()
5-class relation ()
5-drawing. (done)
"""
import numpy
from transformers import pipeline

import classExtraction
import helperFunctions
from ClassEntity import ClassEntity
from hellpingFiles import concept



if __name__ == '__main__':
    # get sentences
    file = helperFunctions.getFile ()
    sentences = helperFunctions.getSentencesFromFile ( file )

    # removes determinants , aux verbs and adjectives.

    sentencesPreprocessed=helperFunctions.preprocess(sentences)
    sentences1=helperFunctions.reduceSentences(sentencesPreprocessed)
    classesFromFreq=concept.getClassesFromFrequency ( sentences )

    ClassEntities=[]
    for classs in classesFromFreq:
        classEnt=ClassEntity(classs)
        ClassEntities.append(classEnt)

    pclasses = None

    for i,sentence in enumerate(sentences1):
        v = sentences1 [ i].find ( "so that" )

        sentence = sentences1 [ i ] [ 0:v ]

        sentence=sentence+ "."
        attributes = [ ]
        x=sentence
        #print(x)
        pclasses=classExtraction.extractClasses(x)
        #print(pclasses)
        for word in pclasses:
            #if doesnt exits then its an attribute
            if not helperFunctions.isExists(word,classesFromFreq):
                if classExtraction.isAttribute(word):
                    attributes.append(word)
        #if not found in main classes due to frequency . then its an attribute .
        #helperFunctions.displayRender ( x )
        found=None
        print ( attributes )
        for att in attributes:
            found = False
            for entity in ClassEntities:
                if  helperFunctions.isExists(att,entity.classAttributes):
                    found=True
            if not found:
                classExtraction.findPossible_ClassFor_Att ( att, classesFromFreq, ClassEntities )




