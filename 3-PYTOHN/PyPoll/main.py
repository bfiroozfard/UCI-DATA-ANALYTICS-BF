'''
The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote.
'''
# import required module
import os
import csv
import sys

#make 3 empty list for 3 columns of CSV file .
voter_id=[]
county=[]
candidate=[]

# set the part to import to python
election_csv = os.path.join("Resources", "election_data.csv")


#open the CSV file
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #find the heade , column names,
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #fill the 3 list for the column info
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])        
    #print(voter_id[0:5])
    #print(county[0:5])
    #print(candidate[0:5])

    #calculate total vote 
    total_vote=len(voter_id)

    #find list of candidate by using set 
    candiate_list=list(set(candidate))
    #print(candiate_list)

    #calculate votes for each calculate . set initial as 2 in a list
    count_vote_each=[0 for i in candiate_list ]
    
    for i in range(len(candiate_list)):
        for j in candidate:
            if candiate_list[i]==j:
                count_vote_each[i]+=1
    #print(count_vote_each)

    #calculate percentage of the vote for each candiate 
    percentage_vote_each=[int((i/total_vote)*10000)/100  for i in count_vote_each]
    #print(percentage_vote_each)

    # sort the candidate by their votes 
    copy_count_each=count_vote_each.copy()
    copy_count_each.sort(reverse=True)
    #for i  in range(len(candiate_list)):
    #    iindex=count_vote_each.index(copy_count_each[i])
    #    print (candiate_list[iindex],count_vote_each[iindex],percentage_vote_each[iindex])
     
    # calculate who is the winner   
    #iindex=count_vote_each.index(copy_count_each[0])
    #print ('winner : ',candiate_list[iindex])

    
    # print the result 
    '''
    Election Results
    -------------------------
    Total Votes: 3521001
    -------------------------
    Khan: 63.000% (2218231)
    Correy: 20.000% (704200)
    Li: 14.000% (492940)
    O'Tooley: 3.000% (105630)
    -------------------------
    Winner: Khan
    -------------------------
    '''
    print('Election Results')
    print ('----------------------------')
    print(f'Total Votes:{total_vote}')
    print('----------------------------')
    for i  in range(len(candiate_list)):
        iindex=count_vote_each.index(copy_count_each[i])
        print(f'{candiate_list[iindex]}: {percentage_vote_each[iindex]} % ({count_vote_each[iindex]})')
    print ('----------------------------')   
    iindex=count_vote_each.index(copy_count_each[0])
    print(f'winner : {candiate_list[iindex]}')
    print ('----------------------------') 
    
    #save result as text 
    sys.stdout = open('result.txt', 'w')
    print('Election Results')
    print ('----------------------------')
    print(f'Total Votes:{total_vote}')
    print('----------------------------')
    for i  in range(len(candiate_list)):
        iindex=count_vote_each.index(copy_count_each[i])
        print(f'{candiate_list[iindex]}: {percentage_vote_each[iindex]} % ({count_vote_each[iindex]})')
    print ('----------------------------')   
    iindex=count_vote_each.index(copy_count_each[0])
    print(f'winner : {candiate_list[iindex]}')
    print ('----------------------------') 
    sys.stdout.close()
    
    
    
     
    
    
    
        