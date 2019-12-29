; Q1
;;;funcs = (double square add-one)
(define (compose-all funcs)
 	(if (null? funcs)
 		(lambda (x) x)
 		(lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
)

; Q2
(define (tail-replicate x n)
  (define (inner l n_in)
  	   (if (= n_in 0)
  	   	   l
  	   	   (inner (cons x l) (- n_in 1)))
  	   )
  (inner nil n)
)