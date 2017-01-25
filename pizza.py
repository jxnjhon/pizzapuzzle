#Attempting to solve the pizza problem for the HashCode competition 2017
#sample input file saved as input.txt


input = open("input.txt", "rt")
instructions = []
for line in input:
    instructions.append(line.strip())
input.close()
rows_cols = instructions[0].split(' ')[0:2] #extracting rows and columns from the file
contents = instructions[1:]                 #extracting the pizza contents
for i in range(int(rows_cols[0])):          #printing the picture of the pizza
    print(contents[i])
    print()

min_ing_per_slice = instructions[0].split(' ')[2]
max_cells_per_slice = instructions[0].split(' ')[-1]

def one_slice(piza, size, start): #function to cut out one slice of any size without holes starting from any col but any row
    one_slice = []                # for start coords i have used zero based coords so that the frst line is 0,0 not 1,1

    if size[1] > len(piza[start[1]:]) or size[0] > len(piza[0][start[0]:]): #check if slice size can fit in pizza
        return ('Size too big for this piza')

    else:
        new_piza = piza[start[1]:]
        for row in new_piza[0:size[1]]:
            new_row = row[start[0]:]
            slice_row = new_row[0:size[0]]
            one_slice.append(slice_row)
        return one_slice
    



print('these are all the instructions:',instructions)
print('these are all the contents: {}'.format(contents))
print('these is the min ingredients per slice:',min_ing_per_slice)
print('these are the max cells per slice:',max_cells_per_slice)
print(one_slice(contents,[3,2], [2,1]))
