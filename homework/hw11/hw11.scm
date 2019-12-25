;;; A cycle with infinite elements inside for instance a linked list which 
;;; have loop inside will never ends.
;;; To solve this question, use two pointers which move at a different speed and check
;;; whether these two pointers will points to the same elements.
(define (find s predicate)
  (if (null? s)
  	  #f
  	  (if (predicate (car s))
  	  	  (car s)
  	  	  (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (if (null? s)
  	  nil
  	  (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k)))
)

(define (has-cycle s)
  ;;; Define a inner function which will keep track of two different stream
  ;;; x moves only one while y moves at two
  (define (inner x y)
  	  (if (or (null? x) (null? y))
  	  	  #f
  	  	  (if (null? (cdr-stream y))
  	  	  	  #f
  	  	  	  (if (eq? (car x) (car (cdr-stream (cdr-stream y))))
  	  	  	  	  #t
  	  	  	  	  (inner (cdr-stream x) (cdr-stream (cdr-stream y)))))))


  (inner s (cdr-stream s))
)
(define (has-cycle-constant s)
      (define (inner x y)
  	  (if (or (null? x) (null? y))
  	  	  #f
  	  	  (if (null? (cdr-stream y))
  	  	  	  #f
  	  	  	  (if (eq? (car x) (car (cdr-stream (cdr-stream y))))
  	  	  	  	  #t
  	  	  	  	  (inner (cdr-stream x) (cdr-stream (cdr-stream y)))))))


  (inner s (cdr-stream s))
)
