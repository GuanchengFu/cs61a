(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
    (map (lambda (s) (append (list first) s))  rests)
)



(define (zip pairs)
  'replace-this-line)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (enum s k)
      (if (null? s)
          nil
          (begin (define k (+ k 1))
                 (cons (cons k (cons (car s) nil)) (enum (cdr s) k))))
  )
  (enum s (- 1))
  )
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
;; cons-all will not evaluate to the right value if the rests is nil
(define (list-change total denoms)
        ;;; If this condition is reached, the related element will be nil.
        ;;; because (cons-all item nil) = nil.
        ;;; This condtion will remove all the bad conditions.
        ;;; For instance (list-change 10 '(5 2)) will not have the (5 2 2 2)
        (cond ((or (null? denoms) (<= total 0)) nil)
              ((< total (car denoms)) (list-change total (cdr denoms)))
              ;;; This is the base case.  The last step of any list-change
              ;;; is when the total equals to one of the elements of denoms.
              ((equal? total (car denoms)) (append (list (list total))
                                                   (list-change total (cdr denoms))))
              (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
                            (list-change total (cdr denoms)))))
        )
  ; BEGIN PROBLEM 18


  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         (cdr expr)
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )))
