

CS341 L05 | September 18, 2019

## Divide and Conquer

> Multiplying Large Numbers. For two n-digit numbers, $\Theta(n^2)$

When doing this in school, this method takes $\Theta(n^2)$ time. But we can do much better than that if we divide and conquer. We will pad with zeros to get equal length numbers.

So lets say we have $981\times 1234$. So then $981\to 0981$, then we have $09|81 \times 12|34$. The operations we do now are

| Operation     | Shift |
| ------------- | ----- |
| $09\times 12$ | 4     |
| $09\times 34$ | 2     |
| $81\times 12$ | 2     |
| $81\times 34$ | 0     |

Then we split this up again, for $0|9 \times 1|2$, etc...

| Operation   | Shift |
| ----------- | ----- |
| $0\times 1$ | 2     |
| $0\times 2$ | 1     |
| $9\times 1$ | 1     |
| $9\times 2$ | 0     |

Which results in $000 + 00 + 90 + 18 = 108$. Notice we *always* add 4 items together, so what’s the recurrence relation?

$T(n)=4T(\frac n2) + O(n)$ . We can now apply the ==Master Theorem==: $T(n) = aT(\frac nb) + c\cdot n^k$. In this situation, $a=4, b=2,k=1$. Looking at $a$ vs $b^k$, we get $4 > 2^1$. Therefore according to Master Theorem, $T(n)\in\Theta(n^{\log_ba})$.

We haven’t improved upon the previous solution so far though! Now notice how we can actually avoid one of the 4 multiplications. If $w=09,x=81,y=12,z=34$, then we get that their product is $(10^2w+x)\times(10^2y+z)\times(10^4wy)\times10^2(wz+xy)+xz$. Consider $(w+x)(y+z)=wy+(wz+xy)+xz$. Here we want the $wz+xy$ term, so we’ll compute the other parts! Let $r=(w+x)(y+z)$. Compute:

- $p=wy$                                   ($09\times12=108$)
- $q=xz$                                    ($81\times34 = 2754$)
- $r=(w+x)(y+z)$               ($90\times 46=4140$)

Then we return $10^4p + 10^2(r-p-q)+q$, which is equivalent to the product. What’s the runtime of this?

$T(n)=3T(\frac n2)+O(n)$, then with Master Theorem, $a=3,b=2,k=1$. Looking at $a$ vs $b^k$, $3 > 2$, therefore we get that $T(n)\in\Theta(n^{\log_ba}) = \Theta(n^{\log_23})$.

> **<u>Exercise</u>**: Multiplying 2 complex numbers (ie. $(a+bi)(c+di)$)

Similar to what we did above! Notice how $(a+bi)(c+di) = ac +(ad+bc)i-bd$, and $(a+b)(c+d)=ac+(ad+bc)+bd$. We set $r=(a+b)(c+d), 

>Multiplying matrices $n\times n$. 

Strassen.