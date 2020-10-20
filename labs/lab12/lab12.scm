; Lab 14: Final Review

; scm> (define (square x) (* x x))
; square
; scm> (define (add-one x) (+ x 1))
; add-one
; scm> (define (double x) (* x 2))
; double
; scm> (define composed (compose-all (list double square add-one)))
; composed
; scm> (composed 1)
; 5

(define (compose-all funcs)
  (if (null? funcs) (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))
      )  
  )
)