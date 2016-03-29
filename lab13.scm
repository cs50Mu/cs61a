;;;;;;;;;;;;;
;; Testing ;;
;;;;;;;;;;;;;

;; function tester -- Used in doctests
;; DO NOT EDIT THE FOLLOWING CODE
(define (assert-equal test-num func-name actual-result expected-result)
  (display (string-append "Testing case " (number->string test-num) " for " func-name ": "))
  (if (not (equal? expected-result actual-result))
      (begin
	(display "Failed.\n")
	(display "Expected: ")
	(display expected-result)
	(display " Got: ")
	(display actual-result)
	(newline)
	(newline))
      (display "Passed!\n")))


;;;;;;;;;;;;;
;; Streams ;;
;;;;;;;;;;;;;


(define multiples-of-three
  (cons-stream 3
	       (stream-map (lambda (x) (+ x 3)) multiples-of-three)
  )

;; tests for multiples-stream
(assert-equal 1 "multiples-stream"
	      (ss multiples-of-three)
	      '(3 6 9 12 15 18 21 24 27 30 ...))


(define (find stream predicate)
  (cond ((stream-null? stream) 'okay)
	((predicate (stream-car stream)) (stream-car stream))
	(else (find (stream-cdr stream) predicate))))

; tests for find
(define m (cons-stream 1 (cons-stream 2 the-empty-stream)))
(assert-equal 1 "find" (find m even?) 2)
(assert-equal 2 "find" (find m (lambda (x) (= x 3))) 'okay)
(assert-equal 3 "find" (find m (lambda (x) (= x 1))) 1)


(define (cycle lst)
  (if (null? lst)
    the-empty-stream
    (cons-stream (car lst)
		 (cycle (append (cdr lst) (list (car lst)))))))   ; append !!

; tests for cycle
(define n '(1 2 3))
(assert-equal 1 "cycle" (ss (cycle n)) '(1 2 3 1 2 3 1 2 3 1 ...))
(define o nil)
(assert-equal 2 "cycle" (cycle o) the-empty-stream)



;;;;;;;;;;;;;;;;;;;;
;; Tail Recursion ;;
;;;;;;;;;;;;;;;;;;;;

(define (question-a x)
  (if (= x 0)
      0
      (+ x (question-a (- x 1)))))

(define (question-b x y)
  (if (= x 0)
      y
      (question-b (- x 1) (+ y x))))

(define (question-c x y)
  (if (= x y)
      #t
      (if (< x y)
	  #f
	  (or (question-c (- x 1) (- y 2)) #f))))

(define (question-d x y)
  (cond ((= x y) #t)
	((< x y) #f)
	(else (or #f (question-d (- x 1) (- y 2))))))


(define (last s)
  (if (null? (cdr s))
    (car s)
    (last (cdr s))))

; Sanity test for last
(assert-equal 1 "last" (last '(1 2 3)) 3)

(define (filter pred lst)
  (define (wrapper lst result)
    (cond ((null? lst) result)
	  ((pred (car lst)) (wrapper (cdr lst) (cons (car lst) result)))
	  (else (wrapper (cdr lst) result))))
  (wrapper lst nil))

; Sanity tests for filter
(assert-equal 1 "filter" (filter (lambda (x) (= x 2)) '(1 1 1 1)) '())
(assert-equal 2 "filter" (filter (lambda (x) (= x 2)) '(2 2 2)) '(2 2 2))
(assert-equal 3 "filter" (filter (lambda (x) (odd? x)) '(1 2 3 4)) '(1 3))

;;;;;;;;;;;;;;
;; Optional ;;
;;;;;;;;;;;;;;

(define (starts-with-a lst sublst)
  (or (null? sublst)
      (and (equal? (car lst) (car sublst))
	   (starts-with-a (cdr lst) (cdr sublst)))))

(define (starts-with-b lst sublst)
  (or (null? sublst)
      (and (starts-with-b (cdr lst) (cdr sublst))
	   (equal? (car lst) (car sublst)))))

(define (starts-with lst sublst)
  (or (and (equal? (car lst) (car sublst))
	   (starts-with (cdr lst) (cdr sublst)))
      (null? sublst)))

; Note: Helper code will help!
(define naturals
  (cons-stream 0
	       (stream-map (lambda (x) (+ x 1))
			   naturals)))

(define (factorial n)
  (if (<= n 1)
    1
    (* n (factorial (- n 1)))))

(define (compute-term x count)
  (* (/ 1 (factorial count)) (expt x count)))

(define (term-stream x) (stream-map (lambda (count) (compute-term x count)) naturals))

(define (add-streams a b)
  (if (equal? a the-empty-stream)
    a
    (if (equal? b the-empty-stream)
      b
      (cons-stream (+ (stream-car a) (stream-car b))
		   (add-streams (stream-cdr a) (stream-cdr b))))))

(define (e-to-the x)
  (cons-stream (stream-car (term-stream x))
	       (add-streams (stream-cdr (term-stream x)) (e-to-the x))))

; Test for e-to-the
; UNCOMMENT WHEN READY TO TEST
; (assert-equal 1 "e-to-the"
;   (< (abs (- (stream-ref (e-to-the 2) 10) 7.3890561)) 0.0001)  stream-ref用于取stream中的某项
;   #t)


(define (power-series x compute-term)
  (define (term-stream x)
    (stream-map (lambda (count) (compute-term x count)) naturals))
  (cons-stream (stream-car (term-stream x))
	       (add-streams (stream-cdr (term-stream x)) (power-series x compute-term))))

;; tests for power-series
(define (sine-term x count)
  (* (/ (expt -1 count) (factorial (+ (* 2 count) 1)))
     (expt x (+ (* 2 count) 1))))
;; Do not change this test
(define sin-series (power-series 3 sine-term))
; UNCOMMENT WHEN READY TO TEST
; (define error (< (abs (- (stream-ref sin-series 10) (sin 3))) 0.00001))
; (assert-equal 1 "power-series" error #t)

