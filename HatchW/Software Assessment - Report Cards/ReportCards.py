import sys
import csv
import json

def readFiles():
    list = []
    for i in range(1,6):
        try:
            directory_name=sys.argv[i]
            list.append(directory_name)
        except:
            if(i == 1):
                print('Please pass path-to-courses-file')
            elif(i == 2):
                print('Please pass path-to-students-file')
            elif(i == 3):
                print('Please pass path-to-tests-file')
            elif(i == 4):
                print('Please pass path-to-marks-file')
            elif(i == 5):
                print('Please pass path-to-output-file')
    return list

def openFiles(directoryArr):
    dict={'courses': [], 'students': [], 'tests': [], 'marks': []}
    for i in range(0,len(directoryArr)-1):
        print()
        if('courses' in directoryArr[i] ):
            arr = dict['courses']
        elif('students' in directoryArr[i] ):
            arr = dict['students']
        elif('tests' in directoryArr[i] ):
            arr = dict['tests']
        elif('marks' in directoryArr[i] ):
            arr = dict['marks']

        with open(directoryArr[i]) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                arr.append(row)
                line_count += 1
            print(f'file {directoryArr[i]}')
            print(f'Processed {line_count} lines.')
    return dict

def parseStudent(data):
    dict={ "students" : []}
    for i in range(0,len(data['students'])):
        courses=[]
        for x in range(0,len(data['marks'])):
            if (data['marks'][x]['student_id'] == data['students'][i]['id']):
                for y in range(0,len(data['tests'])):
                    if(data['marks'][x]['test_id'] == data['tests'][y]['id']):
                        mark= int(data['marks'][x]['mark'])
                        weight= int(data['tests'][y]['weight'])/100
                        grade= mark * weight
                        if not any( int(d['id']) == int(data['tests'][y]['course_id']) for d in courses):
                            for z in range(0,len(data['courses'])):
                                if(int(data['courses'][z]['id']) == int(data['tests'][y]['course_id'])):
                                    name= data['courses'][z]['name']
                                    teacher= data['courses'][z]['teacher']
                                    grades= grade
                                    
                            courses.append({
                                "id": int(data['tests'][y]['course_id']),
                                "name": name,
                                "teacher": teacher,
                                "courseAverage": round(grades,2)
                            })
                        else:
                            for q in range(0,len(courses)):
                                if(int(courses[q]['id']) == int(data['tests'][y]['course_id'])):
                                    courses[q]["courseAverage"]= round(courses[q]["courseAverage"] + grade,2)
        count = 0
        total = 0
        for q in range(0,len(courses)):
            count = count + 1
            total= total + courses[q]["courseAverage"]
        totalAverage = total/count

        student= {
            "id": int(data['students'][i]['id']),
            "name": data['students'][i]['name'],
            "totalAverage": round(totalAverage,2),
            "courses": courses
        }
        dict['students'].append(student)
    return dict

def validator(data):
    courseID = []
    for i in range(0,len(data['tests'])):
        if data['tests'][i]['course_id'] not in courseID:
            courseID.append(data['tests'][i]['course_id'])
    for x in courseID:
        count = 0
        for y in range(0,len(data['tests'])):
            if data['tests'][y]['course_id'] == x:
                count= count + int(data['tests'][y]['weight'])
        if count != 100:
            return False
    return True

def writeFile(dict,arg):
    with open(arg[4], 'w') as outfile:
        json.dump(dict, outfile)

def main():
    directories= readFiles()
    parsedData= openFiles(directories)
    isValid = validator(parsedData)
    if isValid == True:
        students= parseStudent(parsedData)
        writeFile(students,directories)
    else:
        writeFile( {"error" : "Invalid course weights"} ,directories)

if __name__ == "__main__":
    main()