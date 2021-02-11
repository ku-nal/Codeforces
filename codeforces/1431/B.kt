/*  Python Implementation
test=inpi()
while test:
    st=inp()
    ans=0
    i=0
    while i<len(st):
        if st[i]=="w":
            ans+=1
            
        elif i+1<len(st) and st[i]=="v" and st[i+1]=="v":
            ans+=1
            i+=1
        i+=1
    P(ans)
    test-=1
 */          

fun main()= repeat(readLine()!!.toInt())
{
    var s : String = readLine()!!.toString()
    var ans = 0
    var l=s.length
    var i = 0
    while (i < s.length)
    {
        if (s[i] == 'w') 
        {
            ans+=1
        }
        else if((i+1)<l && s[i]=='v' && s[i+1]=='v'){
            ans+=1
            i+=1
        }
        i+=1
    }
    println(ans)
}
