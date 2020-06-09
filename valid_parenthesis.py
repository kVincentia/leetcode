class Solution:
    def isValid(self, s: str) -> bool:
        pastParens = [] #create empty list to store the open p, act as stack
        for i in range(len(s)):
            if self.isOpenParen(s[i]): #check if open
                pastParens.append(s[i]) #store inside stack
            else: #not an open p
                if len(pastParens)==0: #stack is already empty
                    return False
                
                op = pastParens.pop() #the last item in stack, open p
                cl = s[i] #is a close p
                isValid = self.parenIsSameType(op,cl) #compare if same
                if not isValid: 
                    return False
        return len(pastParens)==0 
    #if all matched and stack alr empty then true
    #if all matched but remaining open p, then false
    
    def isOpenParen(self, p):
        if p=='(' or p == '[' or p == '{':
            return True #alr exit from this
        return False #since not an open p then false
    def parenIsSameType(self, op, cl):
        if op =='(' and cl == ')':
            return True
        elif op =='[' and cl == ']':
            return True
        elif op =='{' and cl == '}':
            return True
        else:
            return False
