bool isPalindrome(int x){
{
  int t=x;
  unsigned int sum=0;
  int r=0;
  while(x>0)
  {
     r=x%10;
     sum=(sum*10)+r;
     x=x/10;
  }
  if (sum==t) return 1;
  else return 0;
}
}

