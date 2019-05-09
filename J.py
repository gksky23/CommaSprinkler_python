from functools import reduce
import operator
import functools


def head(l):
	if len(l)==0: return([])
	else:
		li=list(l)
		return(li[0])

def last(l):
	if len(l)==0: return([])
	else:
		li=list(l)
		li.reverse()
		return(li[0])

def forwardAppend(s,l):
	return([s]+l)

def backwardAppend(s,l):
	return(l+[s])

def listToString(l):
	[a]=l
	return a

def f(a):
	if len(a)==1:
		return(a)
	else:
		s,s1,*ss=a
		if not(head(s1)==',' or head(s1)=='.') and (last(s)==',' or last(s)=='.'):
			return forwardAppend(s,f(forwardAppend((last(s)+s1),ss)))		
		elif (head(s1)==','or head(s1)=='.')and not((last(s)==',') or (last(s)=='.')):
			return forwardAppend((s+head(s1)),f(forwardAppend(s1,ss)))
		else: return forwardAppend(s,f(forwardAppend(s1,ss)))

def foldr(func, acc, xs):
	return functools.reduce(lambda x,y: func(y,x), xs[::-1],acc)

def foldl(func, acc, xs):
	return functools.reduce(func, xs, acc)

def lambdaGl(acc,x):
	if(head(x)==','):
		return backwardAppend(1,acc)
	else:
		return backwardAppend(0,acc)

def lambdaGll(acc,x):
	if(last(x)==','):
		return backwardAppend(1,acc)
	else:
		return backwardAppend(0,acc)

def g(lis):
	return foldl(lambdaGl,[],lis)		

def gll(lis):
	return foldl(lambdaGll,[],lis)

def findHeadComma(commaList,intList):
	return [fx(c,i) for (c,i) in zip(commaList, intList)]

def findLastComma(commaList,intList):
	return [fx(c,i) for (c,i) in zip(commaList,intList)]

def fx(c,i):
	if(i==1):
		return c
	else:
		return []

def trimm(lis):
	return foldl(lambdaTr,[],lis)

def lambdaTr(acc,x):
	if not(x):
		return acc
	else:
		return backwardAppend(x,acc)

def delHead(lis):
	return list(map(lambdaDh,lis))

def delLast(lis):
	return list(map(lambdaDl,lis))

def lambdaDh(x):
	return x[1:]

def lambdaDl(x):
	return x[:-1]

def delLastComma(lis):
	if not lis:
		return []
	else:
		return list(map(lambdaDlc,lis))

def lambdaDlc(x):
	if(last(x)==',' or last(x)=='.'):
		return x[:-1]
	else:
		return x

def delHeadComma(lis):
	if not lis:
		return []
	else:
		return list(map(lambdaDhc,lis))

def lambdaDhc(x):
	if (head(x)==',' or head(x)=='.'):
		return x[1:]
	else:
		return x

def addHeadComma(lis,c):
	if not c:
		return lis
	else:
		return list(map(lambda ci: list(map(lambda li: lambdaAhc(ci,li),lis)),c))
		#return list(map(lambda x: list(map(lambda y: lambdaAhc(x,y),lis)),c))

def lambdaAhc(ci, li):
	if ci==head(li):
		return(','+li)
	else:
		return li

def addLastComma(lis,c):
	if not c:
		return lis
	else:
		return list(map(lambda ci: list(map(lambda li: lambdaAlc(ci,li),lis)),c))

def lambdaAlc(ci,li):
	if ci==last(li):
		return(li+',')
	else:
		return li

def compareAc(a,c):
	if len(a)>len(c):
		return a
	else:
		if len(a)<len(c):
			return c
		else:
			if a==c:
				return a
			else:
				if a>c:
					return(head(c)+a)
				else:
					return(head(a)+c)

def zipComma(re):
	return reduce(lambda xs, acc: lambdaZc(xs,acc),re)

def lambdaZc(xs,acc):
	return [compareAc(x,ac) for(x,ac) in zip(xs,acc)]

def ff(l):
	return zipComma(addHeadComma(f(l.split()),delLast(delHead(trimm(findHeadComma(f(l.split()),g(f(l.split()))))))))

def ffll(l):
	return zipComma(addLastComma(f(l.split()),delHead(delLast(trimm(findLastComma(f(l.split()),gll(f(l.split()))))))))

def sumComma(l,li):
	return zipComma([l,li])

def delHeadComma(lis):
	s,*ss=lis
	if head(s)==',' or head(s)=='.':
		return [s[1:]]+ss
	else:
		return lis

def mf(lis):
	if(f(lis.split()==delHeadComma(sumComma(ff(lis),ffll(lis))))):
		return f(lis.split())
	else:
		return mf(" ".join(delHeadComma(sumComma(ff(lis),ffll(lis)))))



def nothingHappen(a):
	if len(a)==1:
		return(a)
	else:
		s,s1,*ss=a
		return forwardAppend(s,nothingHappen(forwardAppend(s1,ss)))
		
