#include<bits/stdc++.h>
#include<stdlib.h>
using namespace std;

struct node{
    int data;
    struct node *left;
    struct node *right;
    int color;// 1=red 0=black
    struct node *parent;
};
struct node *root;

struct node *siblibg(struct node * root){
    if(root==root->parent->right){
        return root->parent->left;
    }
    else if(root=root->parent->left){
        return root->parent->right;
    }
}

struct node *uncle(struct node *root){
    return siblibg(root->parent);
}

struct node *BSTinsert(struct node *root,int key){
    if(root==NULL){
        root=(struct node *)malloc(sizeof(struct node));
        root->data=key;
        root->left=NULL;
        root->right=NULL;
        root->color=1;
        root->parent=NULL;
        return root;
    }
    else if(key>root->data){
        root->right=BSTinsert(root->right,key);
        root->right->parent=root;
        return root;
    }
    else if(key<root->data){
        root->left=BSTinsert(root->left,key);
        root->left->parent=root;
        return root;
    }
}

void inorder(struct node *root){
    if(root==NULL){
        return ;
    }
    inorder(root->left);
    cout<<"(data="<<root->data<<"parent="<<root->parent->data<<")"<<endl;
    inorder(root->right);
}

struct node *corrections(struct node *root){

}
int main(){
    root=NULL;
    root=BSTinsert(root,10);
    root=BSTinsert(root,20);
    root=BSTinsert(root,5);
    root=BSTinsert(root,2);
    root=BSTinsert(root,7);
    root=BSTinsert(root,11);
    root=BSTinsert(root,42);
    inorder(root);
}