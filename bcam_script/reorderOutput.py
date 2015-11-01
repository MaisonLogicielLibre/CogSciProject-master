import os.path
import csv
import time
import glob

cwd = os.getcwd()
file = 'data' + os.path.sep + 'Subject_*'+ os.path.sep +'*.csv'
input_file = os.path.join(cwd,file)

def reorderOutput(input_file):
#    input_file = welcome[0]
#    output_file = welcome[1]
    for filename in glob.glob(input_file):
        fileName, fileExtension = os.path.splitext(filename)
        output_file = fileName + '_ordered'+fileExtension
        print filename
        if  os.path.lexists(filename):
            if os.path.isfile(filename):
                # read file
                writenames = "expName,date,Subject,Session,Handedness,Language,Task Name,Question,Answers,Reaction Time,#RT's >3 STD,Simple RT_Median,Simple RT_Mean,Simple RT STD,Words-IM_6-0,Words-IM_7-0,Words-IM_2-0,Words-IM_1-0,Words-IM_4-0,Words-IM_3-0,Words-IM_5-0,Words-IM_8-0,Words-IM_6-1,Words-IM_7-1,Words-IM_2-1,Words-IM_1-1,Words-IM_4-1,Words-IM_3-1,Words-IM_5-1,Words-IM_8-1,Words-IM_6-2,Words-IM_7-2,Words-IM_2-2,Words-IM_1-2,Words-IM_4-2,Words-IM_3-2,Words-IM_5-2,Words-IM_8-2,Flanker_Cong RT,Flanker_Inc RT,Flanker_Cong RT Var,RT Flanker Effect,Corsi Forward Span,Corsi Reverse Span,History,Sheep,Fruit,Majority,Profession,Music Instrument,Furniture,Clothing,S2Back Omission error,S2Back Hit Rate,S2Back False Alarm,S2Back d-Prime,L2Back Omission error,L2Back Hit Rate,L2Back False Alarm,L2Back d-Prime,L3Back Omission error,L3Back Hit Rate,L3Back False Alarm,L3Back d-Prime".split(",")
                reader = csv.DictReader(open(filename, "rb"))
                writer = csv.DictWriter(open(output_file, "wb"), fieldnames=writenames)
                reorderfunct = lambda r: dict([(col, r[col]) for col in writenames])
                writer.writeheader()
                for row in reader:
                    writer.writerow(reorderfunct(row))
            else:
                print "Selected path is not file"
        else:
            raise ValueError("%s isn't a file!" % filname)
if __name__ == "__main__":
#    try:
#        welcome = welcomescript.runWelcomeScript()
#    except:
#        raise sys.exit()
#    time.sleep(5)
    reorderOutput(input_file)
