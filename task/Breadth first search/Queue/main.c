#include <stdio.h>
#include<stdbool.h>
#define MAX 6

int array[MAX];
int front=0;
int rear=-1;
int itemCount=0;


bool isFull(){
return itemCount==MAX;
}
bool isEmpty(){
return itemCount==0;
}
int dequeue(){
int data=array[front];
front++;
if (front==MAX){
    front=0;
}
itemCount--;
return data;
}
void enqueue(int data){
if(!isFull()){
    if (rear==MAX-1){
        rear=-1;
    }
    array[++rear]=data;
    itemCount++;
}
}
int main(){


}

