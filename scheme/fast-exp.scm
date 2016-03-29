; CS 61A Summer 2014
; Name:
; Login:

(define (assert-equal v1 v2)
  (if (equal? v1 v2)
    (print 'ok)
    (print (list v2 'does 'not 'equal v1))))




;;;;;;;;;;;;;;
;; OPTIONAL ;;
;;;;;;;;;;;;;;

(define (square x) (* x x))

(define (fast-exp-recursive b n)
  (cond ((= n 0)
	 1)
        ((even? n)
	 (square (fast-exp-recursive b (/ n 2))))
        (else
	 (* b (fast-exp-recursive b (- n 1))))))

(define (compound fun1 fun2) (lambda (x) (fun1 (fun2 x))))
	 
(define (fast-exp b n)
  ;; Computes b^n tail recursively by the method of repeated squaring.
  (define (wrapper b n result)
	(cond ((= n 0) 1)
		  ((= n 1) (result b))
		  ((even? n) (begin (define result (compound result square)) (wrapper b (/ n 2) result)))
		  (else (begin (define result (compound result (lambda (x) (* b x)))) (wrapper b (- n 1) result)))))
  (wrapper b n (lambda (x) x))
)


(define (test-fast-exp)
  (assert-equal 8 (fast-exp 2 3))
  (assert-equal 1 (fast-exp 9.137 0))
  (assert-equal 1024 (fast-exp 4 5))
  (assert-equal 6.25 (fast-exp 2.5 2))
  ;; Takes about a second or so if implemented with a
  ;; logarithmic number of steps
  (assert-equal 36 (remainder (fast-exp 2 (fast-exp 2 20)) 100))
  ;; Takes about 10 seconds.  Will crash if not tail recursive.
  (assert-equal 1 (fast-exp 1 (- (fast-exp 2 20000) 1)))

)

(test-fast-exp)
