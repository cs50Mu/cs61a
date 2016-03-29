; CS 61A Summer 2014
; Name:
; Login:

;; function tester -- Used in doctests
;; DO NOT EDIT THE FOLLOWING CODE
(define (assert-equal test-num func-name actual-result expected-result)
  (display (string-append "Testing case " (number->string test-num) " for " func-name ": "))
  (if (not (equal? expected-result actual-result))
      (begin
	(display "Failed.") (newline)
	(display "Expected: ")
	(display expected-result)
	(display " Got: ")
	(display actual-result)
	(newline)
	(newline))
      (begin (display "Passed!") (newline))))


;;;;;;;;;;;;;;;;;;;;;;;
;; Q2: Where's Waldo ;;
;;;;;;;;;;;;;;;;;;;;;;;

(define (wheres-waldo lst)
  (cond ((null? lst) 'nowhere)
        ((equal? (car lst) 'waldo) 0)
        (else
	 (let ((found-him (wheres-waldo (cdr lst))))
	   (if (equal? 'nowhere found-him)
	       'nowhere
	       (+ (wheres-waldo (cdr lst)) 1)
)))))

(define (test-waldo)
  (assert-equal 1 "wheres-waldo" (wheres-waldo '(moe larry waldo curly)) 2)
  (assert-equal 2 "wheres-waldo" (wheres-waldo '(1 2)) 'nowhere))

(test-waldo)


;;;;;;;;;;;;;;;;;;;;;;
;; Q5: Partial Sums ;;
;;;;;;;;;;;;;;;;;;;;;;


(define (partial-sums stream)
  'YOUR-CODE-HERE)

;; Doctests for partial-sums
(define finite
  (cons-stream 2
    (cons-stream 0
      (cons-stream 1
        (cons-stream 4 ())))))

(define ones (cons-stream 1 ones))
(define twos (cons-stream 2 twos))
(define nats (cons-stream 1 (stream-map 1+ nats)))

(define (test-partial-sums)
  (assert-equal 1 "partial-sums"
		(ss (partial-sums twos))
		'(2 4 6 8 10 12 14 16 18 20 ...))
  (assert-equal 2 "partial-sums" 
		(ss (partial-sums (interleave ones twos)))
		'(1 3 4 6 7 9 10 12 13 15 ...))
  (assert-equal 3 "partial-sums"
		(ss (partial-sums finite))
		'(2 2 3 7))
  (assert-equal 4 "partial-sums"
		(ss (partial-sums nats))
		'(1 3 6 10 15 21 28 36 45 55 ...)))

(test-partial-sums)


;;;;;;;;;;;;;;;;;;
;; Q6: Integers ;;
;;;;;;;;;;;;;;;;;;

(define nats
  (cons-stream 1
    (stream-map (lambda (x) (+ x 1)) nats)))

(define integers
  'YOUR-CODE-HERE)

;; Note:  This will infinite loop if you call it on an infinite stream
;; that does not have the element.
(define (has-element? elem stream max-size)
  (and (not (stream-null? stream))
       (> max-size 0)
       (or (equal? elem (stream-car stream))
	   (has-element? elem (stream-cdr stream) (- max-size 1)))))

(define (test-integers)
  (assert-equal 1 "integers" (has-element? 0 integers 1000) #t)
  (assert-equal 2 "integers" (has-element? 12 integers 1000) #t)
  (assert-equal 3 "integers" (has-element? -23 integers 1000) #t))

(test-integers)


;;;;;;;;;;;;;;
;; Optional ;;
;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;
;; Q7: Rationals ;;
;;;;;;;;;;;;;;;;;;;

(define (pairs s t)
  'YOUR-CODE-HERE)

(define rationals
  (pairs nats nats))

(define (test-rationals)
  (assert-equal 1 "rationals" (has-element? 1 rationals 1000) #f)
  (assert-equal 2 "rationals" (has-element? '(1 1) rationals 1000) #t)
  (assert-equal 3 "rationals" (has-element? '(1 2) rationals 1000) #t)
  (assert-equal 4 "rationals" (has-element? '(3 4) rationals 1000) #t)
  (assert-equal 5 "rationals" (has-element? '(4 3) rationals 1000) #t)
  (assert-equal 6 "rationals" (has-element? '(5 2) rationals 1000) #t))

;; Uncomment the following line to test rationals:
; (test-rationals)


