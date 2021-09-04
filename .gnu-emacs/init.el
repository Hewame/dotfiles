;; global configuration
(org-babel-load-file
 (expand-file-name "config.org" user-emacs-directory))

(org-babel-load-file
 (expand-file-name "keybinding.org" user-emacs-directory))

(org-babel-load-file
 (expand-file-name "helpers.org" user-emacs-directory))

;; check operating system
;; use ‘C-h v system-type’ (command ‘describe-variable’) to see the current value of ‘system-type’
(cond ((eq system-type 'gnu/linux)
       ;; Linux-specific code goes here.
       (org-babel-load-file 
         (expand-file-name "linux.org" user-emacs-directory))
       )

      ((eq system-type 'darwin)
       ;; OSX-specific code goes here.
       (org-babel-load-file
         (expand-file-name "darwin.org" user-emacs-directory))
       ))

;; EOF
;; EOF
;; EOF
