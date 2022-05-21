/* A Simple server listening on TCP bof server
   from hackthebox:pozitron, https://github.com/Realradioactive*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

int copier(char *str) {
	char buffer[1024];
	strcpy(buffer, str);
}
void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
	 setgid(0); setuid(0);
     int sockfd, newsockfd, portno,prt;
     printf("Welcome to fury message server  ");
     printf("Type in a server port no:");
     scanf("%d",&prt);
     socklen_t clilen;
     char buffer[4096], reply[5100];
     struct sockaddr_in serv_addr, cli_addr;
     int n;
     sockfd = socket(AF_INET, SOCK_STREAM, 0);
     if (sockfd < 0) 
        error("ERROR opening socket");
     bzero((char *) &serv_addr, sizeof(serv_addr));
     portno = prt;
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);
     if (bind(sockfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0) 
              error("ERROR on binding");
     listen(sockfd,5);
     clilen = sizeof(cli_addr);
     newsockfd = accept(sockfd, 
                 (struct sockaddr *) &cli_addr, 
                 &clilen);
     if (newsockfd < 0) 
          error("ERROR on accept");
     while (1) {
        n = write(newsockfd,"hi fury,to my server!  Type in a message!\n",43);
        bzero(buffer,4096);
        n = read(newsockfd,buffer,4095);
        if (n < 0) error("ERROR reading from socket");

        // CALL A FUNCTION WITH A BUFFER OVERFLOW VULNERABILITY
        copier(buffer);

        printf("Here is the message: %s\n",buffer);
        strcpy(reply, "I got this message: ");
        strcat(reply, buffer);
        n = write(newsockfd, reply, strlen(reply));
        if (n < 0) error("ERROR writing to socket");
        }
     close(newsockfd);
     close(sockfd);
     return 0; 
}
