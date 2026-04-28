# Example Defect Reports

## Defect 001: Locked-out user cannot access inventory

**Status:** Expected behavior  
**Severity:** Medium  
**Priority:** Medium  

### Steps to Reproduce

1. Open SauceDemo login page
2. Enter username: `locked_out_user`
3. Enter password: `secret_sauce`
4. Click Login

### Expected Result

User should see a clear error message explaining the account is locked.

### Actual Result

Error message appears:

```text
Epic sadface: Sorry, this user has been locked out.
```

### Evidence

Covered by automated test:

```text
tests/test_login.py::test_locked_out_user_sees_error_message
```

---

## Defect 002: Checkout form requires first name

**Status:** Expected behavior  
**Severity:** Low  
**Priority:** Medium  

### Steps to Reproduce

1. Log in as `standard_user`
2. Add item to cart
3. Go to cart
4. Click Checkout
5. Leave first name empty
6. Click Continue

### Expected Result

User should see validation message.

### Actual Result

Error message appears:

```text
Error: First Name is required
```

### Evidence

Covered by automated test:

```text
tests/test_checkout.py::test_checkout_requires_first_name
```
