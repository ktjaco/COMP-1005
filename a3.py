from __future__ import division

#defines a function which poses a question, 4 possible answers, and the correct answer
def pose_question(question, answer_a, answer_b, answer_c, answer_d, correct_answer):
	
	print question #prints the question within the function
	print answer_a #prints option a
	print answer_b #prints option b
	print answer_c #prints option c
	print answer_d #prints option d
	
	print "Enter your answer:"	#enter what you believe the correct answer is
	your_answer = raw_input()	#raw input of either (a,b,c, or d)
	
	if your_answer == correct_answer:	#if your answer is equal to the correct answer you'll get 1 point
		print "Yes! That is the correct answer. You get 1 point."
		return 1
	else:	#if not (else) you get it wrong, you get 0 points
		print "Nope! That is the wrong answer."
		return 0

still_play = True #still playing is assigned to True
while still_play == True: #still play is the same as True

	#call my pose_question(...) questions
	
	#Q1 and calculates a score for Q1 (either a 1 or 0)
	score1 = pose_question("What is the capital city of Canada?", "a. Montreal", "b. Toronto", "c. Ottawa", "d. Kingston", "c")
	
	#Q2 and calculates a score for Q2
	score2 = pose_question("What is the capital city of Ontario?", "a. Toronto", "b. London", "c. Ottawa", "d. Kingston", "a")
	
	#Q3 and calculates a score for Q3
	score3 = pose_question("What street is Carleton located on?", "a. Riverside", "b. Elgin", "c. Carling", "d. Colonel By", "d")
	
	#Q4 and calculates a score for Q4
	score4 = pose_question("What are Carleton's sports teams named after?", "a. Winterhawks", "b. Ravens", "c. Gophers", "d. GeeGees", "b")
	
	#Q5 and calculates a score for Q5
	score5 = pose_question("What is Ottawa's NHL team called?", "a. Senators", "b. Ravens", "c. Maple Leafs", "d. Red Wings", "a")
	
	print #prints a new line
	
	total_score = score1 + score2 + score3 + score4 + score5 #a total score for each of the 5 questions
	print "Your total score was %d/5" % total_score #prints your total score
	
	print #prints a new line
	
	if total_score >= 4: #if your total score is equal to or greater than 4 print "Wow, an impressive score!"
		print "Wow, an impressive score!"
	elif total_score == 3: #if your total score is equal to 3 print "Not a bad score.."
		print "Not a bad score.."
	elif total_score < 3: #if your total score is less than 3 print "Better luck next time.."
		print "Better luck next time.."
		
	print #prints a new line
	
	print "Would you like to play again? (Yes or No)" #prints and asks the user if they would like to play again
	keep_playing = raw_input() #input either a yes or no
	keep_playing = keep_playing.lower() #assignment that allows the user to input an upper or lower case letter
	
	if keep_playing == "yes": #if the answer to keep playing is yes..
		still_play == True #play the while loop again
	else: #else it is no
		still_play == False #still play is not true so exit the guiz
		exit() #exits the quiz