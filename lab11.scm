; Runs doctests
; function tester -- Used in doctests
; DO NOT EDIT THE FOLLOWING CODE
(define (assert-equal test-num func-name actual-result expected-result)

    (if (not (equal? expected-result actual-result))
        (begin
            (display  (string-append "Testing case " (number->string test-num) " for " func-name ": Test failed. "))
            (display "Expected: ")
            (display expected-result)
            (display " Got: ")
            (display actual-result)
            (newline)
        )
    )
)

(define (add-one a) 
  (+ a 1)
)

(define (multiply-by-two a) 
  (* a 2)
)

(define (greater-than-zero? a)
  (> a 0)
)

(define (even? a) 
  (= 0 (modulo a 2))
)

; DON'T EDIT ABOVE THIS LINE


; Q1

; Cubes the input x
(define (cube x)
  (* x x x)
)  

; Doctests for cube

; cube test 1
(assert-equal 1 "cube" (cube 2) 8)

; cube test 2
(assert-equal 2 "cube" (cube 3) 27)

; cube test 3
(assert-equal 3 "cube" (cube 1) 1)

; cube test 4 
(assert-equal 4 "cube" (cube 45) 91125)

; Q2
; Outputs a symbol for whether x is equals, over, or under y
(define (over-or-under x y) 
  (if (= x y)
    'equals
    (if (< x y)
      'under
      'over))
  
)

; Doctests for over-or-under

; over-or-under test 1
(assert-equal 1 "over-or-under" (over-or-under 5 5) 'equals)

; over-or-under test 2
(assert-equal 2 "over-or-under" (over-or-under 4 5) 'over)

; over-or-under test 3
(assert-equal 3 "over-or-under" (over-or-under 5 3) 'under)

; Q3
(define (fizzbuzz x)
  'YOUR-CODE-HERE
)

; Doctests for fizzbuzz

; fizzbuzz test 1
; multiple of three and five
(assert-equal 1 "fizzbuzz" (fizzbuzz 15) 'fizzbuzz) 

; fizzbuzz test 2
; multiple of three but not a multiple of five
(assert-equal 2 "fizzbuzz" (fizzbuzz 3) 'fizz)

; fizzbuzz test 3
; multiple of three but not a multiple of five
(assert-equal 3 "fizzbuzz" (fizzbuzz 9) 'fizz) 

; fizzbuzz test 4
; multiple of five but not a multiple of three
(assert-equal 4 "fizzbuzz" (fizzbuzz 5) 'buzz) 

; fizzbuzz test 5
; not a multiple of three or five
(assert-equal 5 "fizzbuzz" (fizzbuzz 14) 14) 

; Q4
(define (gcd a b)
  'YOUR-CODE-HERE
)

; Doctests for gcd

; gcd test 1
(assert-equal 1 "gcd" (gcd 0 4) 4) 

; gcd test 2
(assert-equal 2 "gcd" (gcd 8 0) 8) 

; gcd test 3
(assert-equal 3 "gcd" (gcd 34 19) 1) 

; gcd test 4
(assert-equal 4 "gcd" (gcd 39 91) 13) 

; gcd test 5
(assert-equal 5 "gcd" (gcd 20 30) 10) 

; gcd test 6
(assert-equal 6 "gcd" (gcd 40 40) 40)

; Q5
(define (make-adder num) 
  'YOUR-CODE-HERE
) 

; Doctests for make-adder

(define add-two (make-adder 2))
(define add-three (make-adder 3))

; make-adder test 1
(assert-equal 1 "make-adder" (add-two 2) 4)

; make-adder test 2
(assert-equal 2 "make-adder" (add-two 3) 5)

; make-adder test 3
(assert-equal 3 "make-adder" (add-three 3) 6)

; make-adder test 4
(assert-equal 4 "make-adder" (add-three 9) 12)

; Q6
(define (composed f g)
  'YOUR-CODE-HERE
)

; Doctests for composed

; composed test 1
; (+ (+ x 1) 1)
(assert-equal 1 "composed" ((composed add-one add-one) 2) 4)

; composed test 2
; (* (* x 2) 2)
(assert-equal 2 "composed" ((composed multiply-by-two multiply-by-two) 2) 8)

; composed test 3
; (+ (* x 2) 1)
(assert-equal 3 "composed" ((composed add-one multiply-by-two) 2) 5)

; composed test 4
; (* (+ x 1) 2)
(assert-equal 4 "composed" ((composed multiply-by-two add-one) 2)  6)

; composed test 5
; (+ (+ (+ x 1) 1) 1)
(assert-equal 5 "composed" ((composed (composed add-one add-one) add-one) 2) 5)

; composed test 6
; (+ (+ (* x 2 ) 1) 1)
(assert-equal 6 "composed" ((composed (composed add-one add-one) multiply-by-two) 2) 6) 

; composed test 7
; (* (+ (+ x 1) 1) 2)
(assert-equal 7 "composed" ((composed multiply-by-two (composed add-one add-one)) 2) 8)

; Q7
(define structure 'YOUR-CODE-HERE)

; Doctest for structure
(assert-equal 1 "structure" structure '((1) 2 (3 . 4) 5))

; Q8
(define (filter f lst)
  'YOUR-CODE-HERE
)

; Doctest for filter

; filter test 1
(assert-equal 1 "filter" (filter greater-than-zero? '(1 2 3)) '(1 2 3))

; filter test 2
(assert-equal 2 "filter" (filter greater-than-zero? '()) '())

; filter test 3
(assert-equal 3 "filter" (filter greater-than-zero? '(-2 -2 4 -8)) '(4))

; filter test 4
(assert-equal 4 "filter" (filter even? '(2 3 5 1 6)) '(2 6))

; Optional Section

; Q9
(define (remove item lst)
  'YOUR-CODE-HERE
)

; Doctests for remove

; remove test 1
(assert-equal 1 "remove" (remove 1 '(2 5 1 3)) '(2 5 3))

; remove test 2
(assert-equal 2 "remove" (remove 1 '()) '())

; remove test 3
; remove removes all occurences of the element
(assert-equal 3 "remove" (remove 1 '(1 1 1 1)) '())

; remove test 4
(assert-equal 4 "remove" (remove 1 '(2 5 1 6 1 2)) '(2 5 6 2))

; Q10
(define (all-satisfies lst pred)
  'YOUR-CODE-HERE
)

; Doctests for all-satisfies

; all_satisfies test 1
(assert-equal 1 "all-satisfies" (all-satisfies '(1 2 3 4) greater-than-zero?) #t)

; all_satisfies test 2
(assert-equal 2 "all-satisfies" (all-satisfies '(1 2 -1 4) greater-than-zero?) #f)

; all_satisfies test 3
(assert-equal 3 "all-satisfies" (all-satisfies '(1 2 -1 4) even?) #f)

; all_satisfies test 4
(assert-equal 4 "all-satisfies" (all-satisfies '( 2 -2 4) even?) #t)

