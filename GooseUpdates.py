# GOOSE UPDATES ===============================================================

# This file acts as the backbone of the game. It's main purpose is to update
@@ -49,61 +50,31 @@
Chemicals = ["NaCl (Sodium Chloride)", "NH3 (Ammonia)", "NH4OH (Ammonium Hydroxide)", "HCl (Hydrochloric Acid)", "NaOH (Sodium Hydroxide)"] # [NP] List of possible chemicals to receive in an order

 # [LAW] Instructions for each order
NaClin = ''' Sodium Chloride:
            - Step 1 Given the equation is Na + Cl -> NaCl, you need 
            to dispense equal molar quantities of these elements to 
            the moles of the ordered chemical. This is done by pressing 
            and holding the buttons corresponding to the elements. 
            - Step 2 Click the mix button once you have reached the 
            desired moles of each of your reactants. If you are unhappy 
            with the result, just click the mix button again.
            - Step 3 If you are happy with your result click the done button
            - If the accuracy of the amount you produce is below 30%, you will fail the order'''
NH3in = ''' Ammonia:
            - Step 1 Given the equation is N + 3H -> NH3, you need to 
            dispense stoichiometric molar quantities of these elements 
            to make the moles of the ordered chemical. This is done by 
            pressing and holding the buttons corresponding to the elements. 
            - Step 2 Click the mix button once you have reached the desired 
            moles of each of your reactants. If you are unhappy with the result, 
            just click the mix button again.
            - Step 3 If you are happy with your result click the done button
            - If the accuracy of the amount you produce is below 30%, you will fail the order'''
NH4OHin = ''' Ammonium Hydroxide:
           - Step 1 This is a two-step process, firstly you need to make 
           Ammonia. Given The equation N + 3H -> NH3 you need to dispense 
           stoichiometric molar quantities of these elements to make the moles 
           of the ordered chemical. This is done by pressing and holding the 
           buttons corresponding to the elements
           - Step 2 Now click mix once you have reached the desired moles of 
           each of your first reactants.The next equation is NH3 + O + 2H -> NH4OH 
           you need to dispense equal molar quantities of these elements to the 
           moles of the ordered chemical
           - Step 3 Again now click the mix button once you have reached the desired 
           moles of each of your reactants. If you are unhappy with the result, 
           just click the mix button again.
            - Step 4 If you are happy with your result click the done button. 
            - If the accuracy of the amount you produce is below 30%, you will fail the order
'''
HClin = ''' Hydrochloric Acid:
            - Step 1 Given the equation is H + Cl -> HCl, you need to dispense 
            equal molar quantities of these elements to the moles of the ordered 
            chemical. This is done by pressing and holding the buttons corresponding 
            to the elements. 
            - Step 2 Click the mix button once you have reached the desired moles 
            of each of your reactants. If you are unhappy with the result, just 
            click the mix button again.
            - Step 3 If you are happy with your result click the done button
            - If the accuracy of the amount you produce is below 30%, you will fail the order'''
NaOHin = ''' Sodium Hydroxide:
            - Step 1 Given the equation is Na + O + H  -> NaOH, you need to
            dispense equal molar quantities of these elements to the moles 
            of the ordered chemical. This is done by pressing and holding 
            the buttons corresponding to the elements. 
            - Step 2 Click the mix button once you have reached the desired 
            moles of each of your reactants. If you are unhappy with the result, 
            just click the mix button again.
            - Step 3 If you are happy with your result click the done button
            - If the accuracy of the amount you produce is below 30%, you will fail the order'''

ChemicalCorrelator = {"H2O (Water)": FlaskC, "NH4OH (Ammonium Hydroxide)": FlaskB, "NH3 (Ammonia)": FlaskB} # [NP] Matches each chemical with an appropriate sprite
ChemicalClassification = {"H2O (Water)": mol.H2O(), "NH4OH (Ammonium Hydroxide)": mol.NH4OH(), "NH3 (Ammonia)": mol.NH3(), "NaCl (Sodium Chloride)": mol.NaCl(), "HCl (Hydrochloric Acid)": mol.HCl(), "NaOH (Sodium Hydroxide)": mol.NaOH()}
@@ -113,7 +84,7 @@

# GAME SETTINGS ===============================================================

QuantityRange = [1, 50] # [NP] The range of quantity of a chemical a customer can order
QuantityRange = [1, 100] # [NP] The range of quantity of a chemical a customer can order
TextFont = "Calibri" # [NP] The font the game uses
CustomerSpeed = 1 # [NP] Multiplies the customer walk speed
FlaskSpeed = 1 # [NP] Multiplies the flask conveyor speed
@@ -125,7 +96,7 @@
SpeechBubbleSize = (550, 550)
MachineSize = (1300, 800)
FlaskSize = (200, 250)
FontSizes = [40, 18]
FontSizes = [40, 25]

BigCLSize = [700, 400, 50, 50] 
SmallCLSize = [700, 50, 50, 50]
@@ -279,7 +250,7 @@ def mixing_sequence(): # [LG] function that returns true to allow if statement t

# STARTING THE GAME ===========================================================

def Game(Score, time_allowed): # [NP] The score parameter determines how much score the player has
def Game(Score): # [NP] The score parameter determines how much score the player has

# TEXT FUNCTIONS ==============================================================    

@@ -316,7 +287,8 @@ def display_text2(text, x, y):
    font2 = pygame.freetype.SysFont(TextFont, FontSizes[1])

# TIMER FUNCTIONS===============================================================
   
    time_given = 1000 # [LAW] The amount the timer will cound down for
    begin=pygame.time.get_ticks()# [LAW] Initial time


    def display_timer(count_down, initial,fail_time):
@@ -332,9 +304,9 @@ def display_timer(count_down, initial,fail_time):
        timer_text = 'Remaining Time: ' + str(int(remaining_time))
        display_text(timer_text, 900 ,50)# [LAW] Displays the time on the screen

    #def elapsed(initial): ([KY]: no longer needed, time elapsed is defined correctly before the point assignment)
        #player_time_elapsed = ((pygame.time.get_ticks()-initial) / 1000)# [LAW] Calculates the elapsed time of the player once done making the chemical
        #return player_time_elapsed
    def elapsed(initial):
        player_time_elapsed = ((pygame.time.get_ticks()-initial) / 1000)# [LAW] Calculates the elapsed time of the player once done making the chemical
        return player_time_elapsed



@@ -383,7 +355,7 @@ def display_timer(count_down, initial,fail_time):
    FlaskMoves = MoveFrames // FlaskSpeed
    mixing_start = False
    OrderOver = False
    Order_points = 0
    OrderPoints = 0

# CUSTOMER CREATION ===========================================================

@@ -403,7 +375,7 @@ def display_timer(count_down, initial,fail_time):

    for i in range(len(Chemicals)): # [LAW] Finds what Chemical has been ordered and assigns the instructions to the instructions variable
        if Chemicals[i] in orderchem:
           instructions = 'You are making ' + str(ordercapacity) + ' Moles of ' + instruction_list[i]
            instructions = instruction_list[i]

# LOADING FLASKS ==============================================================

@@ -455,21 +427,17 @@ def display_timer(count_down, initial,fail_time):
                running = False  # [LAW] Allows the window to be closed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos) and not show_machine:  # [LAW] Check if the click is within the first button's area ("Accept Order")
                if button_rect.collidepoint(mouse_pos) and not show_machine:  # [LAW] Check if the click is within the first button's area
                    Show_things = True
                    Show_FlaskCOPY = True
                    time_at_beginorder = pygame.time.get_ticks()/1000 #[KY] get time in seconds that have elapsed from beginning of the game to the start of the order ("Accept Order" being pressed)
                    time_given = time_allowed # [LAW] The amount the timer will count down for, initialized once accept order is pressed
                    begin=pygame.time.get_ticks()# [LAW] Initial time
                elif button_rect2.collidepoint(mouse_pos) and not show_machine:  # [LAW] Check if the click is within the second button's area ("Quit")
                elif button_rect2.collidepoint(mouse_pos) and not show_machine:  # [LAW] Check if the click is within the second button's area
                    running = False
                elif click_area3.collidepoint(mouse_pos) and show_machine: # [NP] Check if the DONE button has been clicked
                    FlaskPhase = 0
                    Move_Flask = True
                    Show_FlaskCOPY = False
                    time_at_endorder = pygame.time.get_ticks()/1000 #[KY] get time in seconds that have elapsed from beginning of the game to the end of the order ("Done" being pressed), to be compared with time_at_beginorder to determine points
                elif playagain_rect.collidepoint(mouse_pos) and OrderOver:
                    Game(0,time_allowed)
                    Game(0)
                elif endgame_rect.collidepoint(mouse_pos) and OrderOver:
                    running = False

@@ -492,6 +460,7 @@ def display_timer(count_down, initial,fail_time):


        if show_machine:
            done = False

# STARTING UP THE MIXER =======================================================

@@ -517,10 +486,7 @@ def display_timer(count_down, initial,fail_time):
            Ca_button.draw(screen)
            Mixing_button.draw(screen)
            #===========================================
            """
            function keeps assigning new object to mix1 than mix2 then mix3
            even if mix1 is already defined as that object
            """
            #===========================================
            #Hydrgoen
            if isthesame(mix1,mol.H()): # [LG] Checks if mix1 is already H
@@ -652,7 +618,7 @@ def display_timer(count_down, initial,fail_time):
            # [LAW] Update the display
            pygame.display.flip()

            if display_timer(time_given,begin,False): # [LAW] If the timer runs out displays fail message
            if display_timer(time_given,begin,False) and done == False: # [LAW] If the timer runs out displays fail message
                pygame.draw.rect(screen, BLUE, playagain_rect) # [KY] draws play again and quit game buttons (rects are defined above)
                pygame.draw.rect(screen, RED, endgame_rect) 
                font.render_to(screen, (360, 385), "Game Over - Click to Play Again", WHITE)
@@ -676,13 +642,11 @@ def display_timer(count_down, initial,fail_time):
                pygame.display.update()

        if Show_FlaskCOPY: screen.blit(FlaskCOPY, FlaskCopyPos)  # [LAW] Display FlaskCOPY at the new position
     
        if Move_Flask:
            time_taken = time_at_endorder - time_at_beginorder# [KY] Returns how long it took the player to make the chemical
            time_fraction = (time_given - time_taken)/(time_given) #[KY] returns fraction of time remaining after completing the order, to be used in point function
            
            print(time_taken) #[KY] for testing purposes
            print(time_fraction) #[KY] for testing purposes
            done = True
            time_taken=elapsed(time_given)# [LAW] Returns how long it took the player to make the chemical
            time_difference = time_given - time_taken

            if FlaskPhase < FlaskMoves:
                flask_position.move_ip(FlaskOffset * FlaskSpeed, 0)  # [LAW] Move the Flask
@@ -691,21 +655,18 @@ def display_timer(count_down, initial,fail_time):

# POINT ASSIGNMENT/FAIL CHECK =================================================

                Order_accuracy = accuracy_as_percent(mix1, ChemicalClassification[orderchem], mix1.Quantity, ordercapacity) # [KY] EDIT, Assign accuracy of order to accuracy_as_percent function call
                #[KY] Parameters must correspond to (chemical produced, chemical ordered (good), quantity of chemical produced, quantity of chemical ordered)
                #[KY] If the types of the first two objects aren't equal, accuracy will be 0 (confirmed)
                Order_points = point_calculation(ChemicalClassification[orderchem].Difficulty, Order_accuracy/100, time_fraction) # [KY] Assign points per order to order_match function call
                print("Accuracy:" + str(Order_accuracy) + "\nPoints:" + str(Order_points) + "\nTime taken:" + str(time_taken) + "\nTime given: " + str(time_given) + "\nTime fraction: " + str(time_fraction)) #[KY] for testing purposes
                Order_accuracy = accuracy_as_percent(orderchem, orderchem, ordercapacity, ordercapacity) # [KY] Assign accuracy of order to accuracy_as_percent function call
                OrderPoints = point_calculation(ChemicalClassification[orderchem].Difficulty, Order_accuracy / 100, time_difference) # [KY] Assign points per order to order_match function call
                
                if Order_accuracy < 30: # [KY] Checks if the accuracy of the amount produced compared to the amount ordered is below 30 (fail condition)
                    pygame.draw.rect(screen, BLUE, playagain_rect) # [KY] draws play again and quit game buttons (rects are defined above)
                    pygame.draw.rect(screen, RED, endgame_rect) 
                    font.render_to(screen, (360, 385), "Game Over - Click to Play Again", WHITE)
                    font.render_to(screen, (550, 535), "Quit Game", WHITE)
                    OrderOver = True
                else:
                     Game(Score + Order_points,(time_allowed-5))
                     Game(Score + OrderPoints)
                     time_given -= 2

            FlaskPhase += 1

@@ -720,6 +681,6 @@ def display_timer(count_down, initial,fail_time):

# STARTING THE GAME ===========================================================

Game(0,100) # [NP] Plays The Game.
Game(0) # [NP] Plays The Game.

# END =========================================================================
