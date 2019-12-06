;; Extra Scheme Questions ;;


; Q5  This is the 2019 spring lab version because the 2018 version can not show the picture.
(define lst
  (cons (cons 1 nil)
        (cons 2 
        	  (cons (cons 3 (cons 4 nil)) 
        	  (cons 5 nil))))
)




; Q6  call f(g(x))
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (define (notequal? x)
  	      (if (= x item)
  	      	  #f
  	      	  #t))
    (filter notequal? lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (define max_number (max a b))
  (define min_number (min a b))
  (if (= min_number 0)
  	  max_number
  	  (gcd min_number (modulo max_number min_number)))
  
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
	(if (null? s)
		s
		(cons (car s)
			  (no-repeats (filter (lambda (x) (not (= x (car s))))
			  	                  (cdr s)))))
)

; Q10
(define (substitute s old new)
	(if (null? s)
		s
		(if (pair? (car s))
			(cons (substitute (car s) old new)
				  (substitute (cdr s) old new))
			(if (equal? (car s) old)
				(cons new (substitute (cdr s) old new))
				(cons (car s) (substitute (cdr s) old new)))))
)

; Q11
(define (sub-all s olds news)
  (if (null? s)
  	  s
  	  (if (null? olds)
  	  	  s
  	  	  (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
  	      ))
)