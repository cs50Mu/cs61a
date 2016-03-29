; Some utility functions that you may find useful.

(define (map proc items)
  (if (null? items)
      nil
      (cons (proc (car items))
            (map proc (cdr items)))))

(define (filter predicate sequence)
  (cond ((null? sequence) nil)
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate (cdr sequence))))
        (else (filter predicate (cdr sequence)))))

(define (stream-map proc s)
  (if (stream-null? s)
      the-empty-stream
      (cons-stream (proc (stream-car s))
                   (stream-map proc (stream-cdr s)))))

(define (stream-filter pred stream)
  (cond ((stream-null? stream) the-empty-stream)
        ((pred (stream-car stream))
         (cons-stream (stream-car stream)
                      (stream-filter pred
                                     (stream-cdr stream))))
        (else (stream-filter pred (stream-cdr stream)))))

; display-stream prints out n elements of a stream s. If there is less than n
; elements in the stream, then it will only print the elements in the stream and
; end.
(define (display-stream s n)
  (define (display-line x)
    (display x)
    (newline))
  (define (stream-for-each proc s n)
    (cond ((stream-null? s) 'done)
          ((= n 0) '___done)
          (else (begin (proc (stream-car s))
                (stream-for-each proc (stream-cdr s) (- n 1))))))
  (stream-for-each display-line s n))

(define (interleave s1 s2)
  (if (stream-null? s1)
      s2
      (cons-stream (stream-car s1)
                   (interleave s2 (stream-cdr s1)))))

(define (member? x list)
     (if (null? list) #f
         (if (equal? x (car list)) #t
              (member? x (cdr list)))))

(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))
; Problem 20

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; YOUR CODE HERE
  (cond ((and (null? list1) (null? list2)) nil)
    	((null? list1) list2)
	((null? list2) list1)
	((comp (car list1) (car list2)) (cons (car list1) (merge comp (cdr list1) list2)))
	(else (cons (car list2) (merge comp list1 (cdr list2))))

  )
)

(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Sort a list of lists of numbers to be in decreasing lexicographic
;; order. Relies on a correct implementation of merge.
(define (sort-lists lsts)
  (if (or (null? lsts) (null? (cdr lsts)))
      lsts
      (let ((sublsts (split lsts)))
        (merge greater-list
               (sort-lists (car sublsts))
               (sort-lists (cdr sublsts))))))

(define (greater-list x y)
  (cond ((null? y) #t)
        ((null? x) #f)
        ((> (car x) (car y)) #t)
        ((> (car y) (car x)) #f)
        (else (greater-list (cdr x) (cdr y)))))

(define (split x)
  (cond ((or (null? x) (null? (cdr x))) (cons x nil))
        (else (let ((sublsts (split (cdr (cdr x)))))
                (cons (cons (car x) (car sublsts))
                      (cons (car (cdr x)) (cdr sublsts)))))))

(merge greater-list '((3 2 1) (1 1) (0)) '((4 0) (3 2 0) (3 2) (1)))
; expect ((4 0) (3 2 1) (3 2 0) (3 2) (1 1) (1) (0))


; Problem 21

;; A stream that computes all possible patterns, each of which contain at least
;; one OVER and one UNDER
(define (patterns)
  ; YOUR CODE HERE
  ((cons-stream 
  the-empty-stream)

; Gets the first N items out of stream of patterns into a
; list and sees if items are valid patterns
(define (test-pattern stream-pattern n)
    (cond ((stream-null? stream-pattern) the-empty-stream) 
        ((equal? n 1) (list (stream-car stream-pattern)))
        ((and (member? 'over (stream-car stream-pattern))
            (member? 'under (stream-car stream-pattern)))
                (cons (stream-car stream-pattern)
                    (test-pattern (stream-cdr stream-pattern) (- n 1))))
       (else the-empty-stream)))

; True if ss2 contains all elements of ss1
(define (sol-contains-all ss1 ss2)
    (or (null? ss1)
        (and (member? (car ss1) ss2)
          (sol-contains-all (cdr ss1) ss2))))

;; Gets first 8 items out of patterns. Stops if any item in patterns is not valid.
(define pattern-lst (test-pattern (patterns) 8))

;; Create a list that contains patterns that do happen in the first 8 items of pattern
(define lst '((under over) (over under) (under over over) (over under over) (over over under) 
  (under over under) (under under over)))

;; Checks pattern-list contains the first 8 patterns
(and (equal? (length pattern-lst) 8) (sol-contains-all lst pattern-lst))
; expect #t

; Problem 22

;; The Tree abstract data type has an entry and a list of children.
(define (make-tree entry children)
  (cons entry children))
(define (entry tree)
  (car tree))
(define (children tree)
  (cdr tree))

;; An example tree:
;;                5
;;       +--------+--------+
;;       |        |        |
;;       6        7        2
;;    +--+--+     |     +--+--+
;;    |     |     |     |     |
;;    9     8     1     6     4
;;                      |
;;                      |
;;                      3
(define tree
  (make-tree 5 (list
                (make-tree 6 (list
                              (make-tree 9 nil)
                              (make-tree 8 nil)))
                (make-tree 7 (list
                              (make-tree 1 nil)))
                (make-tree 2 (list
                              (make-tree 6 (list
                                            (make-tree 3 nil)))
                              (make-tree 4 nil))))))

;; Takes a TREE of numbers and outputs a list of sums from following each
;; possible path from root to leaf.
(define (tree-sums tree)
  ; YOUR CODE HERE
  nil)

(tree-sums tree)
; expect (20 19 13 16 11)



; Problem 23 (optional)

; Draw the hax image using turtle graphics.
(define (hax d k)
  ; YOUR CODE HERE
  nil)
