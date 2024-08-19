
public class Solution {
	public  boolean isPalindrome(int s) {
        int d=s;
		int z=0;
		while(s>0) {
			z=z*10+s%10;
			s=s/10;
			
		}
		return z==d;
	}}

	
