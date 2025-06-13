# Stock GUI

This is a GUI made in python with PyQt5 to control stock in the larder cupboard (and later the entire kitchen) in our house so that we never run out of anything. This is to be hosted on a small computer that can be mounted to a screen which can be interacted with. This is also a father's day present because I'm lazy and couldn't think of a better present. 

## GUI 

The GUI is to be made using PyQt5 which I learned developing the [De-Orbiting Satellite](https://github.com/jrobo-gith/De-Orbiting-Satellite-GroupProj) and will include:

\begin{itemize}
\item Navigation through items in the larder cupboard divided into sections such as spices, fruit, and other things. 
\item Able to add or remove items.
\item Able to toggle 're-stock'.
\end{itemize}

## Features
\begin{itemize}
\item List of all items in the larder cupboard with images and descriptions
\item Access to a qualitative stock estimation, with users able to estimate the amount of stock left, i.e, 'half a jar', 'third of a tin'. Along with this, they will see the the number of 'jars' or 'tins' in the cupboard.
\item Qualitative stock estimation will be coupled with a typical serving amount. 
\item Users will be able to mark item's as "re-stock", adding the item to the list of items to buy at the end of the week if the typical servings drop below 1 or 2 servings.
\item The list of items that need re-stocking will be emailed to the person ordering the food for them to add to the order. 
\end{itemize}
