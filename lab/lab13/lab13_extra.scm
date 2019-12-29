; Q4
(define (rle s)
  (define (inner element n s)
          (if (null? s)
              (cons-stream (list element n) nil)
              (if (= element (car s))
                  (inner element (+ n 1) (cdr-stream s))
                  (cons-stream (list element n) (inner (car s) 0 s)))))

  (if (null? s)
      nil
      (inner (car s) 0 s))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  (define (inner before s)
          (cond ((null? s)        (append before (list n)))
                ((< (car s) n)    (inner (append before (list (car s))) (cdr s) ))
                ((<= n (car s))   (append before (append (list n) s)))))
  (inner nil s)
  )

; Q6
(define (deep-map fn s)
  (define (inner before s)
          (cond ((null? s) (append before nil)) 
                ((list? (car s)) (inner (append before (list (deep-map fn (car s)))) (cdr s)))
                (else (inner (append before (list (fn (car s)))) (cdr s)))))
  (inner nil s)
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
;;;(unique '(billy billy bob billy bob billy bob)) = (billy bob)
(define (unique s)
  (define (inner before s)
    (if (null? s)
        before
        (if (inside (car s) before)
            (inner before (cdr s))
            (inner (append before (list (car s))) (cdr s)))))
  (inner nil s)
)

(define (inside name s)
  (if (null? s)
      #f
      (if (eq? name (car s))
          #t
          (inside name (cdr s)))))

(define (count name s)
  (if (null? s)
      0
      (if (eq? name (car s))
          (+ 1 (count name (cdr s)))
          (count name (cdr s))))
)

(define (tally names)
  (define (inner s)
    (if (null? s)
        nil
        (cons (cons (car s) (count (car s) names)) (inner (cdr s)) )))
  (inner (unique names))
)