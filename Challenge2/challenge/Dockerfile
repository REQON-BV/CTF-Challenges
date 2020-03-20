FROM i386/ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server gdb vim sudo python nano binutils-multiarch gcc


RUN mkdir /var/run/sshd

RUN useradd -ms /bin/bash guest
RUN useradd -ms /bin/bash rob

# Button smashing for (semi) random passwords :)
RUN echo 'root:;sdfhgkj;lsdfhgjkl;sdfhgljkhdxfkljghsljkdfhgklsdg' | chpasswd
RUN echo 'rob:sdfgsdfgkjsdflk;gjsdf;klgjs;dlfkgjs;ldfgkjsj;lnm,m' | chpasswd
RUN echo 'guest:Testing123' | chpasswd


COPY ./source/robs_admin_program.c /tmp/robs_admin_program.c
RUN gcc /tmp/robs_admin_program.c -o /usr/bin/robs_admin_program -fno-stack-protector
RUN rm /tmp/robs_admin_program.c

COPY ./source/TODO.txt /home/rob/TODO.txt


RUN chown root:rob /home/rob/
RUN chmod  744 /home/rob/TODO.txt
RUN chown root:root /usr/bin/robs_admin_program
RUN chmod 4555 /usr/bin/robs_admin_program

COPY ./source/flag.txt /home/rob/flag.txt
RUN chown root:rob /home/rob/flag.txt
RUN chmod 740 /home/rob/flag.txt

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
