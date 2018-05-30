!-------Monte Carlo evaluation of pi-------
!By Amol Deshmukh, The City College of New York, 30 April 2018.

program montecarlo

	real::a(10000000),b(10000000),c(10000000)
	real::pi,d
	integer :: i

	call random_number(a) 
	call random_number(b)
	
	do i=1,10000000
		c(i)=sqrt(a(i)*a(i)+b(i)*b(i))
	end do	

	do i=1,10000000
		if (c(i)>1) then
			c(i)=0
		else 
			c(i)=1	
		end if
	end do
		
	d=sum(c)
	pi=d/10000000

	print *,pi*4

end program montecarlo
