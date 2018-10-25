# Midterm Review

> October 24, 2018

---

## Binary Trees

The Big 5 for a Binary Tree:

```c++
struct Binary {
    string content;
    Binary *left;
    Binary *right;
};

Binary(string content, Binary left, Binary right) {
    // do this too
}

~Binary(){
    delete left;
    delete right;
}

Binary(const Binary &other)
: left{other.left ? new Binary{other.left} : nullptr},
	right{other.right ? new Binary{other.right} : nullptr},
    content{other.content} { 
}

Binary & operator=(const Binary &other) {
    using std::swap;
    Binary temp{other};
    swap(temp.left, left);
    swap(temp.right, right);
    swap(temp.content, content);
    return *this;
}
          
Binary &(Binary &&other)
: left{other.left}, right{other.right}, content{other.content} {
    other.left = nullptr;
    other.right = nullptr;
}

Binary & operator=(Binary &&other) {
	std::swap(other.left, left);
    std::swap(other.right, right);
    std::swap(other.content, content);
    return *this;
}

int main(){
    Binary b1{"hello", nullptr, nullptr};
}
```

## Move assignment operator:

When writing a move assignment operator, remember to:

- do a **self assignment check**
- create **deep copies**
- delete old data off the heap

Using the **Copy & Swap Idiom** can bypass having to create deep copies and deleting the old data.