(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start	(- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
   ;;; The newterm for the inner function holds the result for the calculation.
  (define (inner newterm combiner n term)
  		(if (= n 0)
  			newterm
  			(inner (combiner newterm (term n)) combiner (- n 1) term))
  	)
  (inner start combiner n term)
)




(define-macro (list-of expr for var in seq if filter-fn)
  (list 'map (list 'lambda (list var) expr) (list 'filter (car filter-fn) seq))
)